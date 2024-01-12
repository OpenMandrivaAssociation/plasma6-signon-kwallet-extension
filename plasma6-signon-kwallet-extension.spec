%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:        KWallet integration for Sign-on framework
Name:           plasma6-signon-kwallet-extension
Version:	24.01.90
Release:	2
License:        GPLv2+
Group:          System/Base
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/signon-kwallet-extension-%{version}.tar.xz
URL:            https://www.kde.org/
BuildRequires:  cmake(ECM)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(SignOnExtension)
BuildRequires:	cmake(KF6Wallet)

#BuildRequires:  kwallet-devel >= 6.0

%description
KWallet integration for Sign-on framework.

#------------------------------------------------------------------------------

%define keyringkwallet_major 16
%define libkeyringkwallet %mklibname keyring-kwallet %{keyringkwallet_major}

%package -n %libkeyringkwallet
Summary: Runtime library for cantor
Group: System/Libraries
Provides: %{name} = %{EVRD}

%description -n %libkeyringkwallet
Runtime library for %{name}.

%files -n %libkeyringkwallet
%_libdir/signon/extensions/libkeyring-kwallet.so

#------------------------------------------------------------------------------

%prep
%autosetup -p1  -n signon-kwallet-extension-%{?git:master}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
