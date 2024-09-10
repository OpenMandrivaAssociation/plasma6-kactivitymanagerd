%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: plasma6-kactivitymanagerd
Version:	6.1.5
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kactivitymanagerd/-/archive/%{gitbranch}/kactivitymanagerd-%{gitbranchd}.tar.bz2#/kactivitymanagerd-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/kactivitymanagerd-%{version}.tar.xz
%endif
Summary: KDE Plasma 6 Activities
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: boost-devel
Requires: qt6-qtbase-sql-sqlite

%description
KDE Plasma 6 Activities.

%prep
%autosetup -p1 -n kactivitymanagerd-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang kactivities6 || touch kactivities6.lang

%files -f kactivities6.lang
%{_datadir}/qlogging-categories6/kactivitymanagerd.categories
%{_libdir}/libkactivitymanagerd_plugin.so
%{_libdir}/libexec/kactivitymanagerd
%{_prefix}/lib/systemd/user/plasma-kactivitymanagerd.service
%{_datadir}/dbus-1/services/org.kde.ActivityManager.service
%{_datadir}/krunner/dbusplugins/plasma-runnners-activities.desktop
%{_qtdir}/plugins/kactivitymanagerd1
