#!/usr/bin/env python3
"""
Simple HTTP server to serve the quantum-resilient IoT demonstration webpages
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Change to the directory containing the HTML files
    os.chdir(Path(__file__).parent)
    
    PORT = 8080
    
    # Check if port is available
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"🚀 Quantum-Resilient IoT Demo Server")
            print(f"📡 Server running at: http://localhost:{PORT}")
            print(f"🌐 Available pages:")
            print(f"   • Main Demo: http://localhost:{PORT}/quantum_resilient_demo.html")
            print(f"   • Interactive Presentation: http://localhost:{PORT}/interactive_presentation.html")
            print(f"")
            print(f"🎯 For your interview, open the Interactive Presentation:")
            print(f"   http://localhost:{PORT}/interactive_presentation.html")
            print(f"")
            print(f"⏹️  Press Ctrl+C to stop the server")
            print(f"=" * 60)
            
            # Try to open the browser automatically
            try:
                webbrowser.open(f'http://localhost:{PORT}/interactive_presentation.html')
                print(f"🌐 Browser opened automatically")
            except:
                print(f"⚠️  Could not open browser automatically")
            
            print(f"")
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Trying port {PORT + 1}")
            PORT += 1
            with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
                print(f"🚀 Quantum-Resilient IoT Demo Server")
                print(f"📡 Server running at: http://localhost:{PORT}")
                print(f"🌐 Interactive Presentation: http://localhost:{PORT}/interactive_presentation.html")
                print(f"⏹️  Press Ctrl+C to stop the server")
                httpd.serve_forever()
        else:
            print(f"❌ Error starting server: {e}")
            sys.exit(1)
    except KeyboardInterrupt:
        print(f"\n🛑 Server stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    main()
