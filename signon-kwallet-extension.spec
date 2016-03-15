Summary:        KWallet integration for Sign-on framework
Name:           signon-kwallet-extension
Version: 15.12.3
Release:        1
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz

URL:            https://www.kde.org/

BuildRequires:  cmake(ECM)

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)

BuildRequires:  pkgconfig(SignOnExtension)
BuildRequires:	cmake(KF5Wallet)

#BuildRequires:  kwallet-devel >= 5.0

%description
KWallet integration for Sign-on framework

#------------------------------------------------------------------------------

%define keyringkwallet_major 15
%define libkeyringkwallet %mklibname keyring-kwallet %{keyringkwallet_major}

%package -n %libkeyringkwallet
Summary: Runtime library for cantor
Group: System/Libraries

%description -n %libkeyringkwallet
Runtime library for cantor

%files -n %libkeyringkwallet
%_kde5_libdir/signon/extensions/libkeyring-kwallet.so

#------------------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

