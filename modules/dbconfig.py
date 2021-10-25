import os

EMDROS_VERSIONS = [
    "emdros 3.4.0",
    "3.4.1.pre12",
    "emdros 3.5.3",
    "emdros 3.7.3",
]
"""Emdros versions that have been in use by SHEBANQ.

Copied manually from /opt/emdros/include/emdros/version-emdros.h
"""

CONFIG = dict(shebanqUser="shebanq")
"""Connection details for the databases.

Also details about the mailserver and account that can send
shebanq emails to users for the purpose of password verification.
"""

configPath = "/opt/cfg/mql.cfg"
if os.path.exists(configPath):
    with open(configPath) as p:
        CONFIG["shebanqPassword"] = p.read().rstrip("\n")
else:
    CONFIG["shebanqPassword"] = "localpwd"

configPath = "/opt/cfg/host.cfg"
if os.path.exists(configPath):
    with open(configPath) as p:
        CONFIG["shebanqHost"] = p.read().rstrip("\n")
else:
    CONFIG["shebanqHost"] = "localhost"

configPath = "/opt/cfg/mail.cfg"
if os.path.exists(configPath):
    with open(configPath) as p:
        keyValueLines = p.read().split("\n")
        keyValues = {}
        for line in keyValueLines:
            line = line.strip()
            if not line:
                continue
            (key, value) = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            keyValues[key] = value
        CONFIG["mailServer"] = keyValues.get("server", None)
        CONFIG["mailSender"] = keyValues.get("sender", None)
else:
    CONFIG["mailServer"] = "localhost"
    CONFIG["mailSender"] = "shebanq@localhost"
