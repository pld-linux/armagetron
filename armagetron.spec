Summary:	A Tron lightcycle game with focus on multiplayer mode
Summary(pl):	Gra Tron ze ¶wiat³ocyklem skupiaj±ca siê na trybie dla wielu graczy
Name:		armagetron
Version:	0.2.5.2
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	71bfeaa5ddaf38d5fd8d893caec91d15
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	http://armagetron.sourceforge.net/addons/moviepack.zip
# Source3-md5:	e2d40309dde7e1339ca6aff7599cdfa3
URL:		http://armagetron.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
Buildrequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}

%description
In Armagetron, you ride a lightcycle around the game grid. You can
only make sharp turns of 90 degrees and a wall constantly builds up
after you. Make your enemies crash into your wall, but be aware that
they are trying to do the same to you. If you are fast enough, you may
be able to trap them, but the only way to speed up your lightcycle is
to drive close to the dangerous walls. Prepare for exciting strategic
preparations followed by action-packed close combat!

%description -l pl
W grze Armagetron jedzie siê ¶wiat³ocyklem dooko³a planszy. Mo¿na
wykonywaæ tylko ostre zakrêty o 90 stopni, a za graczem ci±gle buduje
siê ¶ciana. Trzeba spowodowaæ, by wrogowie roztrzaskali siê na tej
¶cianie, ale tak¿e uwa¿aæ, bo oni próbuj± zrobiæ to samo. Je¶li gracz
jest szybki, mo¿e z³apaæ ich wszystkich, ale jedynym sposobem na
przyspieszenie ¶wiat³ocyklu jest jazda blisko niebezpiecznych ¶cian.
Trzeba siê przygotowaæ na ekscytuj±ce strategiczne przygotowania i
nastêpuj±c± po nich walkê w zbli¿eniu!

%package moviepack
Summary:	Moviepack addon
Summary(pl):	Dodatek Moviepack
Group:		X11/Applications/Games
Requires:	%{name} = %{version}

%description moviepack
Moviepack addon.

%description moviepack -l pl
Dodatek Moviepack.

%prep
%setup -q -a 3

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_prefix}/games/%{name}/moviepack

%{__make} install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

cp -R moviepack $RPM_BUILD_ROOT%{_prefix}/games/%{name}
rm -f $RPM_BUILD_ROOT%{_prefix}/games/%{name}/moviepack/art_read_me.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG doc/*.html doc/net
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.srv
%dir %{_prefix}/games/%{name}
%{_prefix}/games/%{name}/arenas
%dir %{_prefix}/games/%{name}/bin
%attr(755,root,root) %{_prefix}/games/%{name}/bin/[ap]*
%dir %{_prefix}/games/%{name}/language
%{_prefix}/games/%{name}/language/languages.txt
%{_prefix}/games/%{name}/language/english.txt
%lang(de) %{_prefix}/games/%{name}/language/deutsch.txt
%{_prefix}/games/%{name}/models
%{_prefix}/games/%{name}/sound
%{_prefix}/games/%{name}/textures
%{_applnkdir}/Games/*
%{_pixmapsdir}/*

%files moviepack
%defattr(644,root,root,755)
%doc moviepack/art_read_me.txt
%{_prefix}/games/%{name}/moviepack
