Summary:     full screen text mode program for playing audio CD's
Summary(de): Vollbildprogramm in Textmodus zum Abspielen von Audio-CDs
Summary(fr): Programme en mode texte plein écran pour lire les CD audio.
Summary(tr): Müzik CD'lerini çalmak için bir metin ekran programý
Name:        cdp
Version:     0.33
Release:     11
Copyright:   GPL
Group:       Applications/Sound
Source:      ftp://sunsite.unc.edu/pub/Linux/apps/sound/cdrom/curses/%{name}-%{version}.tgz
Patch:       cdp-fsstnd.patch
Patch1:      cdp-cdplay.patch
Patch2:      cdp-ncurses.patch
Patch3:      cdp-glibc.patch
BuildRoot:   /tmp/%{name}-%{version}-root

%description
This program allows you to play audio CD's on your computers CDROM drive. It
provides a version with a full screen interface as well as a command line
version.

%description -l de
Mit diesem Programm können Sie die auf dem CD-ROM-Laufwerk Ihres Computers
Audio-CDs abspielen. Es liegt in zwei Versionen vor: Einmal als Voll-
bildschirm-, einmal als Befehlszeilen-Version.

%description -l fr
Ce programme permet de jouer des CDs audio sur le lecteur CDROM. Il offre
une version plein écran et une version en ligne de commande.

%description -l tr
Bu program, bilgisayarýnýzýn CDROM sürücüsünde müzik CD'lerini çalmanýza
yarar. Komut modunda veya tam ekran arayüzüyle kullanabilirsiniz.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make COMP_OPT="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make DESTDIR=$RPM_BUILD_ROOT install
gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Sun Nov 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.33-11]
- added gziping man pages,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using $RPM_OPT_FLAGS during compile,
- added full %attr description in %files.

* Sat Aug 15 1998 Jeff Johnson
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed src url

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
