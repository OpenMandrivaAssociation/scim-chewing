%define version	0.3.191
%define svnrel 830
%define release	%mkrel 2.%{svnrel}.1

%define chewing_version	        0.3.091
%define scim_version		1.4.5

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-chewing
Summary:	SCIM IMEngine module for chewing
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://chewing.csie.net/
Source0:	%{name}-%{version}-r%{svnrel}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	libchewing >= %{chewing_version}
Requires:	scim >= %{scim_version}
BuildRequires:  libchewing-devel >= %{chewing_version}
BuildRequires:  scim-devel >= %{scim_version}
BuildRequires:  intltool gettext-devel

# compatibility
Obsoletes:	%mklibname %{name} 0

%description
Scim-chewing is an SCIM IMEngine module for chewing,
an intelligent Chinese phonetic input method.


%prep
%setup -q -n %name

%build
./autogen.sh AM_VERSION=""
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unnecessary files
rm -f %{buildroot}%{_libdir}/scim-1.0/*/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/icons/*
%{_libdir}/scim-1.0/*/IMEngine/*.so
%{_libdir}/scim-1.0/*/SetupUI/*.so


