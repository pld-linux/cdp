Summary:	full screen text mode program for playing audio CD's
Summary(de):	Vollbildprogramm in Textmodus zum Abspielen von Audio-CDs
Summary(fr):	Programme en mode texte plein écran pour lire les CD audio
Summary(pl):	Pe³noekranowy, tekstowy program do odtwarzania p³yt CD
Summary(tr):	Müzik CD'lerini çalmak için bir metin ekran programý
Name:		cdp
Version:	0.33
Release:	23
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/sound/cdrom/curses/%{name}-%{version}.tgz
Patch0:		%{name}-fsstnd.patch
Patch1:		%{name}-cdplay.patch
Patch2:		%{name}-ncurses.patch
Patch3:		%{name}-glibc.patch
Patch4:		%{name}-strchr.patch
Patch5:		%{name}-FHS20.patch
Patch6:		%{name}-changer.patch
Patch7:		%{name}-keys.patch
Patch8:		%{name}-nonblock.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows you to play audio CD's on your computers CDROM
drive. It provides a version with a full screen interface as well as a
command line version.

%description -l de
Mit diesem Programm können Sie die auf dem CD-ROM-Laufwerk Ihres
Computers Audio-CDs abspielen. Es liegt in zwei Versionen vor: Einmal
als Voll- bildschirm-, einmal als Befehlszeilen-Version.

%description -l fr
Ce programme permet de jouer des CDs audio sur le lecteur CDROM. Il
offre une version plein écran et une version en ligne de commande.

%description -l pl
Ten program pozwala na odtwarzanie p³yt CD w twoim napêdzie. Zawiera
zarówno wersjê z tekstowym interfejsem jak i bez niego.

%description -l tr
Bu program, bilgisayarýnýzýn CDROM sürücüsünde müzik CD'lerini
çalmanýza yarar. Komut modunda veya tam ekran arayüzüyle
kullanabilirsiniz.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%{__make} COMP_OPT="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
