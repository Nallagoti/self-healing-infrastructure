#!/usr/bin/python3

import json
import hmac
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN_FILE = "/etc/prometheus/webhook_token"
RECOVERY_SCRIPT = "/usr/local/sbin/recover-nginx"

class WebhookHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path != "/alert":
            self.send_error(404)
            return

        try:
            with open(TOKEN_FILE, "r") as f:
                expected_token = f.read().strip()

            received_token = self.headers.get("Authorization", "")
            expected_header = "Bearer " + expected_token

            if not hmac.compare_digest(received_token, expected_header):
                self.send_error(401, "Unauthorized")
                return

            length = int(self.headers.get("Content-Length", "0"))

            if length <= 0 or length > 1048576:
                self.send_error(400, "Invalid request size")
                return

            payload = json.loads(self.rfile.read(length))

            alerts = payload.get("alerts", [])

            should_recover = any(
                alert.get("status") == "firing"
                and alert.get("labels", {}).get("alertname") == "NginxDown"
                and alert.get("labels", {}).get("severity") == "critical"
                and alert.get("labels", {}).get("job") == "blackbox-http"
                for alert in alerts
            )

            if not should_recover:
                self.send_response(202)
                self.end_headers()
                self.wfile.write(b"No matching firing alert")
                return

            result = subprocess.run(
                ["/usr/bin/sudo", "-n", RECOVERY_SCRIPT],
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode != 0:
                print("Recovery failed:", result.stderr, flush=True)
                self.send_error(500, "Recovery failed")
                return

            print("NGINX recovery completed successfully", flush=True)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"NGINX recovery completed")

        except Exception as error:
            print("Webhook error:", str(error), flush=True)
            self.send_error(500, "Internal error")

    def log_message(self, format, *args):
        print("Webhook:", format % args, flush=True)


server = HTTPServer(("127.0.0.1", 5000), WebhookHandler)
print("Webhook receiver listening on 127.0.0.1:5000", flush=True)
server.serve_forever()
