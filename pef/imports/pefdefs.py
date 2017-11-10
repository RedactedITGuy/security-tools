# Definitions for pef.py

# exploitable functions
exploitableFunctions = ["system(", "exec(", "popen(", "pcntl_exec(",
                        "eval(", "preg_replace(", "create_function(", "include(", "require(", "passthru(",
                        "shell_exec(", "popen(", "proc_open(",
                        "pcntl_exec(", "asset(", "extract(", "parse_str(", "putenv(", "ini_set(",
                        "mail(", "header(", "unserialize("]

# other keywords points to critical features, credentials, configs etc.
keywords = [
    "api",
    "api_key",
    "api_secret_key",
    "secret_key",
    "secret",
    "BEGIN",
    "PRIVATE",
    "private",
    "PRIVATE_KEY",
    "private_key",
    "key",
    "token",
    "CSRF",
    "Arrays.equals",
    "HMAC",
    "random",
    "mt_rand",
    "rand",
    "random.org",
    "iv",
    "encrypt",
    "crypt",
    "MCRYPT",
    "RIJNDAEL",
    "MCRYPT_RIJNDAEL_256",
    "ECB",
    "ecb",
    "password",
    "passwd",
    "pass",
    "hash",
    "hashlib",
    "hashed",
    "md5",
    "sha1",
    "sha-1",
    "sha2",
    "sha-2",
    "salt",
    "bcrypt",
    "PBKDF2",
    "blake2",
    "CVE",
    "vulnerable",
    "stackoverflow",
    "SO",
    "base64",
    "Base64",
    "admin",
    "rot13",
    "tmp",
    "system",
    "popen",
    "backtick operator",
    "pcntl_exec",
    "eval",
    "preg_replace",
    "create_function",
    "exec",
    "passthru",
    "system",
    "shell_exec",
    "popen",
    "proc_open",
    "pcntl_exec",
    "assert",
    "preg_replace('/.*/e',",
    "create_function",
    "include",
    "include_once",
    "require",
    "require_once",
    # "$_GET",  it's already defined in globalVars below
    "phpinfo",
    "posix_mkfifo",
    "posix_getlogin",
    "posix_ttyname",
    "getenv",
    "get_current_user",
    "proc_get_status",
    "get_cfg_var",
    "disk_free_space",
    "disk_total_space",
    "diskfreespace",
    "getcwd",
    "getlastmo",
    "getmygid",
    "getmyinode",
    "getmypid",
    "getmyuid",
    "extract",
    "parse_str",
    "putenv",
    "ini_set",
    "mail",
    "header",
    "proc_nice",
    "proc_terminate",
    "proc_close",
    "pfsockopen",
    "fsockopen",
    "apache_child_terminate",
    "posix_kill",
    "posix_mkfifo",
    "posix_setpgid",
    "posix_setsid",
    "posix_setuid",
    "chmod",
    "chown",
    "shell=True",
    "pickle.loads",
    "yaml.load"
]
# dangerous global(s)
globalVars = ["$_POST", "$_GET", "$_COOKIE", "$_REQUEST", "$_SERVER"]

# dangerous patterns - LFI/RFI
fileInclude = ["include($_GET", "require($_GET",
               "include_once($_GET", "require_once($_GET",
               "include($_REQUEST", "require($_REQUEST", "include_once($_REQUEST", "require_once($_REQUEST"]

# reflected properties which might leads to eg. XSS
reflectedProperties = ["$_SERVER[\"PHP_SELF\"]",
                       "$_SERVER[\"SERVER_ADDR\"]",
                       "$_SERVER[\"SERVER_NAME\"]",
                       "$_SERVER[\"REMOTE_ADDR\"]",
                       "$_SERVER[\"REMOTE_HOST\"]",
                       "$_SERVER[\"REQUEST_URI\"]",
                       "$_SERVER[\"HTTP_USER_AGENT\"]"]
