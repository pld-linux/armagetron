Summary:	A Tron lightcycle game with focus on multiplayer mode
Summary(pl):	Gra Tron ze ¶wiat³ocyklem skupiaj±ca siê na trybie dla wielu graczy
Name:		armagetron
Version:	0.2.5.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	99c1a776691362108911bbd67e4a27c8
Patch0:		%{name}-ac_fix.patch
URL:		http://armagetron.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
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

%prep
%setup -q
#%patch0 -p1

%build
#rm -f missing
#{__aclocal}
#{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

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
