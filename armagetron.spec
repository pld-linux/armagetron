Summary:	-
Summary(pl):	-
Name:		armagetron
Version:	0.2.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	a1a2a7c6ab93c60d31965dd9ff1e24c5
URL:		http://armagetron.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}

%description

%description -l pl

%prep
%setup -q

%build
#rm -f missing
#{__gettextize}
#{__aclocal}
#{__autoconf}
#{__autoheader}
#{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG doc/*
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}
%{_sysconfdir}/*
%{_prefix}/games/%{name}
