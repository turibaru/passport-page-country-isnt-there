# Contract: copies the invented passport spread (entry.png, an
# illustration of the fictional Republic of Solvenna) to
# /output/entry.png, validating it first. Python stdlib only,
# no network, no randomness: the output is byte-identical to
# the bundled image on every run.
import hashlib
import os
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIM = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_SHA256 = "88a8326a0284b14512255d218a7a5b1576d6330f1e9b27b34a1492362e4012eb"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(here, "entry.png")
    with open(source_path, "rb") as handle:
        data = handle.read()

    # 1. Size limit.
    if len(data) > MAX_BYTES:
        fail(f"entry.png is {len(data)} bytes, over the {MAX_BYTES} limit")

    # 2. PNG magic.
    if data[:8] != PNG_MAGIC:
        fail("entry.png does not start with the PNG magic bytes")

    # 3. Dimensions from the IHDR chunk (width/height are the first
    #    8 bytes of the IHDR data, big-endian uint32).
    if len(data) < 33 or data[12:16] != b"IHDR":
        fail("entry.png has no IHDR chunk where expected")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        fail(f"entry.png is {width}x{height}, over the {MAX_DIM}x{MAX_DIM} limit")

    # 4. Integrity: the bundled image must match its known hash.
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        fail(f"entry.png sha256 mismatch: got {digest}")

    # 5. Write the output (create the directory if needed; never
    #    delete the directory itself or its other contents).
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.png")
    with open(output_path, "wb") as handle:
        handle.write(data)

    # 6. Verify the output is byte-identical.
    with open(output_path, "rb") as handle:
        written = handle.read()
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        fail("output entry.png sha256 mismatch after write")

    print(f"wrote {output_path}: {width}x{height} PNG, "
          f"{len(data)} bytes, sha256 {EXPECTED_SHA256}")


if __name__ == "__main__":
    main()
