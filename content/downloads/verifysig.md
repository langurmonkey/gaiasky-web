+++
title = "Verify GPG signatures"
description = "Learn how to verify our signed packages with GPG"
type = "page"
+++


In this page you will learn how to verify the packages you download from the [downloads]({{< ref "downloads" >}}) section using GPG.

## Why not just use checksums?

Regular checksums (in MD5 or SHA256) provide a way to verify the package integrity, i.e., the package has not been 'corrupted' during the download. However, they are useless to prove that the packages really come from us and have not been tampered with. To achieve this, we use cryptographic signatures via GPG by signing each package with our own personal key.

## Verify a package

If you use **Linux**, you should be able to find your way around easily. On **macOS**, you can use GPGTools. If you are on **Windows**, you can find more information on verifying gpg signatures in the [Tor Project website](https://support.torproject.org/tbb/how-to-verify-signature/).

Ok, first you need to have `gpg` installed and working. For each package that you download from our website, for example `gaiasky-package.zip`, we provide a detached signature file named `gaiasky-package.zip.sig`. This signature is generated with our personal key. In order to verify it, you first need to import the key:

```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys  0x448C2B189756743013D5F7C22FD2A59C1D734C1F
```

You can now verify the signature for each file:

```bash
gpg --verify gaiasky-package.zip.sig gaiasky-package.zip
```

If the verification succeeded, you should see a line "Good signature from [...]" somewhere in the output, like so:

```bash
gpg: Signature made Mon 19 Feb 2024 12:46:08 CET
gpg:                using RSA key 448C2B189756743013D5F7C22FD2A59C1D734C1F
gpg: Good signature from "Antoni Sagrista Selles "
```
<br><br>
{{< iconify "mdi:arrow-left-bold-circle" >}} [Back to downloads]({{< ref "downloads" >}})
