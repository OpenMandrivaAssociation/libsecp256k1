%global oname	secp256k1

%global major	0
%global libname	%mklibname %{oname}_ %{major}
%global devname	%mklibname %{oname} -d

Name:		libsecp256k1
Summary:	Optimized C library for EC operations on curve secp256k1
Version:	0.27.1
Release:	1
License:	MIT
Group:		System/Libraries
Url:		https://github.com/Bitcoin-ABC/secp256k1
Source0:	https://github.com/Bitcoin-ABC/secp256k1/archive/v%{version}/%{oname}-%{version}.tar.gz
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	cmake

%description
Optimized C library for EC operations on curve secp256k1.

Features:
* secp256k1 ECDSA signing/verification and key generation.
* Adding/multiplying private/public keys.
* Serialization/parsing of private keys, public keys, signatures.
* Constant time, constant memory access signing and pubkey generation.
* Derandomized DSA (via RFC6979 or with a caller provided function.)
* Very efficient implementation.

%package -n %{libname}
Summary:	Optimized C library for EC operations on curve secp256k1
Group:		System/Libraries
Provides:	libsecp256k1 = %{EVRD}

%description -n %{libname}
Optimized C library for EC operations on curve secp256k1.

Features:
* secp256k1 ECDSA signing/verification and key generation.
* Adding/multiplying private/public keys.
* Serialization/parsing of private keys, public keys, signatures.
* Constant time, constant memory access signing and pubkey generation.
* Derandomized DSA (via RFC6979 or with a caller provided function.)
* Very efficient implementation.

%package -n %{devname}
Summary:	Development files and headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files and headers for %{name}.

%prep
%setup -qn %{oname}-%{version}

%build
%cmake -DSECP256K1_ENABLE_MODULE_ECDH=ON \
	-DSECP256K1_ENABLE_MODULE_RECOVERY=ON
%make_build

%install
%make_install -C build

#we don't want these
find %{buildroot} -name "*.la" -delete

%check
#make check

%files -n %{libname}
%{_libdir}/libsecp256k1.so.%{major}{,.*}

%files -n %{devname}
%{_includedir}/secp256k1*.h
%{_libdir}/libsecp256k1.so

