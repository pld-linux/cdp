Summary:	Full screen text mode program for playing audio CD's
Summary(de.UTF-8):	Vollbildprogramm in Textmodus zum Abspielen von Audio-CDs
Summary(fr.UTF-8):	Programme en mode texte plein écran pour lire les CD audio
Summary(pl.UTF-8):	Pełnoekranowy, tekstowy program do odtwarzania płyt CD
Summary(tr.UTF-8):	Müzik CD'lerini çalmak için bir metin ekran programı
Name:		cdp
Version:	0.33
Release:	29
License:	GPL
Group:		Applications/Sound
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/sound/cdrom/curses/%{name}-%{version}.tgz
# Source0-md5:	9bf61177d9fba16ddd4c647a182039fc
Patch0:		%{name}-fsstnd.patch
Patch1:		%{name}-cdplay.patch
Patch2:		%{name}-ncurses.patch
Patch3:		%{name}-glibc.patch
Patch4:		%{name}-strchr.patch
Patch5:		%{name}-FHS20.patch
Patch6:		%{name}-changer.patch
Patch7:		%{name}-keys.patch
Patch8:		%{name}-nonblock.patch
Patch9:		%{name}-bo_fix.patch
Patch10:	%{name}-getline.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows you to play audio CD's on your computers CDROM
drive. It provides a version with a full screen interface as well as a
command line version.

%description -l de.UTF-8
Mit diesem Programm können Sie die auf dem CD-ROM-Laufwerk Ihres
Computers Audio-CDs abspielen. Es liegt in zwei Versionen vor: Einmal
als Voll- bildschirm-, einmal als Befehlszeilen-Version.

%description -l fr.UTF-8
Ce programme permet de jouer des CDs audio sur le lecteur CDROM. Il
offre une version plein écran et une version en ligne de commande.

%description -l pl.UTF-8
Ten program pozwala na odtwarzanie płyt CD w twoim napędzie. Zawiera
zarówno wersję z tekstowym interfejsem jak i bez niego.

%description -l tr.UTF-8
Bu program, bilgisayarınızın CDROM sürücüsünde müzik CD'lerini
çalmanıza yarar. Komut modunda veya tam ekran arayüzüyle
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
%patch9 -p1
%patch10 -p1

%build
%{__make} COMP_OPT="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
