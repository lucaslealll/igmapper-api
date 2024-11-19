<div align="center">
<img src="assets/instagram_logo.png" alt="Logo" height="100px"/>
<br><br>

![](https://img.shields.io/badge/Python%20Version-3.10-111?&labelColor=2C6287)
![](https://img.shields.io/badge/%20Version%20-1.0.0-111?&labelColor=2C6287)
![](https://img.shields.io/badge/Status-W.I.P-111?&labelColor=2C6287)
[![](https://img.shields.io/badge/Code%20Style-Black-111?&labelColor=2C6287)](https://github.com/psf/black)

<!-- [![Contributors](https://img.shields.io/github/contributors/lucaslealll/instagram-followers)](https://github.com/lucaslealll/instagram-followers/graphs/contributors/badge/) -->
<!-- [![Artifact HUB](https://img.shields.io/endpoint?url=_____)](_____) -->

<h1><strong>Instagram Followers & Unfollowers</strong></h1>
</div>

## This code aims to:
- List all followers who do not follow the account back;
- List all followers of an *Instagram* account;
- List all followers of an *Instagram* account.

## Install
> [!IMPORTANT]
> It's essential to **upgrade pip** to the latest version to ensure compatibility with the library.
> ```sh
> pip install --upgrade pip
> ```
>
> **Don't forget to install the requirements.**
> ```sh
> pip install -r requirements.txt
> ```

## Run

To run the application, on the terminal run:
```sh
cd <path_to>/instagram-followers
python scripts/main.py
```

### Output
<pre>
<b>Instagram Followers & Unfollowers</b>
<b>Enter the Instagram username (without '@'):</b> athena.mentorship
Cookie file founded...
Retrieving user account ID...

<b>Investigated profile:</b>
    https://www.instagram.com/athena.mentorship
    <b>athena.mentorship</b> 🟓
    <b>0</b> posts     <b>9</b> followers     <b>3</b> following
    <b>Athena Mentorship</b>
    Education
    'Esclareça sua dúvida em um click!
    🧠 Para conectar mentes
    📚 Monitoria certificada online
    👇  Acompanhe nosso desenvolvimento'
    🔗 <b>['https://github.com/athena-mentorship']</b>

Get followers...
Get following...
Building following dictionary...
Building followers dictionary...
Get non followers...

<b>Don't follow back:</b>
  1) User Name A        username_a      https://instagram.com/username_a
  2) User Name B        username_b      https://instagram.com/username_b
  3) User Name C        username_c      https://instagram.com/username_c
<b>Do you want to show the following list? [Y/n]:</b> y
  1) User Name D        username_d      https://instagram.com/username_d
  2) User Name E        username_e      https://instagram.com/username_e
<b>Do you want to show the followers list? [Y/n]:</b> y
  1) User Name F        username_f      https://instagram.com/username_f
  2) User Name G        username_g      https://instagram.com/username_g
</pre>