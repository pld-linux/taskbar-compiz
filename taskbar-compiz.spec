
%define		_kdever	3.5.4
Summary:	taskbar-compiz - modified kicker taskbar for compiz
Summary(pl.UTF-8):	taskbar-compiz - zmodyfikowany pasek zadań dla compiza
Name:		taskbar-compiz
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.kde-apps.org/CONTENT/content-files/49484-%{name}.tar.gz
# Source0-md5:	596cf261cb69f30b21a05ea4290767d4
Patch0:		kde-ac260-lt.patch
Patch1:		kde-am.patch
URL:		http://www.kde-apps.org/content/show.php?content=49484
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-devel
BuildRequires:	kdelibs-devel >= 9:%{_kdever}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a modified taskbar applet for kicker to make it work with
compiz.

Please note: currently you can't change "Show windows from all
desktops" settings while beryl is running, so uncheck it before or
uncheck in manually in ~/.kde/share/config/ktaskbarrc

%description -l pl.UTF-8
To jest zmodyfikowana wersja paska zadań dla KDE, która
współpracuje z compizem.

Notatka: ta wersja nie pozwala na zmianę "Pokazywania okien ze
wszystkich pulpitów" ("Show windows from all desktops") podczas
uruchomionego beryla. Powinieneś edytować
~/.kde/share/config/ktaskbarrc ręcznie.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/compiztaskbar_panelapplet.so
%attr(755,root,root) %{_libdir}/libcompiztaskbar.so*
%attr(755,root,root) %{_libdir}/libcompiztaskmanager.so*
%{_datadir}/apps/kicker/applets/compiztaskbarapplet.desktop
