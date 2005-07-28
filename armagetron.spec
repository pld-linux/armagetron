#
# TODO: start scripts for server
Summary:	A Tron lightcycle game with focus on multiplayer mode
Summary(pl):	Gra Tron ze ¶wiat³ocyklem skupiaj±ca siê na trybie dla wielu graczy
Name:		armagetron
Version:	0.2.6.1
Release:	5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	20c670d6e2bdcae2a3e52a3fab2788b7
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	http://armagetron.sourceforge.net/addons/moviepack.zip
# Source3-md5:	e2d40309dde7e1339ca6aff7599cdfa3
Patch0:		%{name}-types.patch
URL:		http://armagetron.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# it installs data in %{_prefix}/games, so...
%define		_bindir			/usr/bin
%define		_prefix			/usr/%{_lib}
%define		_sysconfdir		/etc/%{name}
%define		_sysconfdir_server 	/etc/%{name}-server

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
Requires:	%{name} = %{version}-%{release}

%description moviepack
Moviepack addon.

%description moviepack -l pl
Dodatek Moviepack.

%package server
Summary:	Armagetron server
Summary(pl):	Serwer Armagetrona
Group:		Applications/Games

%description server
Armagetron server.

%description server -l pl 
Serwer Armagetrona.

%prep
%setup -q -a3
%patch0 -p1

sed -i -e 's@/usr/lib@/usr/%{_lib}@;s@X11R6/lib@X11R6/%{_lib}@' configure.in

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}

%configure \
	--disable-glout 

%{__make} bindist
mv bindist bindist-dedicated
sed -i 's@\/etc\/armagetron@\/etc\/armagetron-server@' bindist-dedicated/bin/starter

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_bindir}} \
	$RPM_BUILD_ROOT%{_prefix}/games/%{name}/moviepack \
	$RPM_BUILD_ROOT%{_sysconfdir_server}

%{__make} install

cd bindist-dedicated
./install
cd ..

mv -f $RPM_BUILD_ROOT%{_prefix}/bin/* $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

cp $RPM_BUILD_ROOT%{_sysconfdir}/* $RPM_BUILD_ROOT%{_sysconfdir_server}
cp -R moviepack $RPM_BUILD_ROOT%{_prefix}/games/%{name}
rm -f $RPM_BUILD_ROOT%{_prefix}/games/%{name}/moviepack/art_read_me.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG doc/*.html doc/net
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.srv
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-stat
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
%{_desktopdir}/*
%{_pixmapsdir}/*

%files moviepack
%defattr(644,root,root,755)
%doc moviepack/art_read_me.txt
%{_prefix}/games/%{name}/moviepack

%files server 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/armagetron-dedicated
%dir %{_prefix}/games/armagetron-dedicated
%{_prefix}/games/armagetron-dedicated/bin
%attr(755,root,root) %{_prefix}/games/armagetron-dedicated/bin/*
%exclude %{_prefix}/games/armagetron-dedicated/bin/uninstall
%{_prefix}/games/armagetron-dedicated/language
%dir %{_sysconfdir_server}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir_server}/*.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir_server}/*.srv
