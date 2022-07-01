%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:        KWallet integration for Sign-on framework
Name:           signon-kwallet-extension
Version:	22.04.1
Release:	2
License:        GPLv2+
Group:          System/Base
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
URL:            https://www.kde.org/
BuildRequires:  cmake(ECM)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(SignOnExtension)
BuildRequires:	cmake(KF5Wallet)

#BuildRequires:  kwallet-devel >= 5.0

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
%_kde5_libdir/signon/extensions/libkeyring-kwallet.so

#------------------------------------------------------------------------------

%prep
%setup -q 
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
