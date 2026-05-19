import os, http.server, functools

os.chdir("/Users/lulutheball/Desktop/Projects/Midnight Sun/.claude/worktrees/nice-bell-f38ebc")
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=os.getcwd())
with http.server.HTTPServer(("", 3456), handler) as httpd:
    httpd.serve_forever()
