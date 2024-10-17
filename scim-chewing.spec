%define version	0.3.4

%define chewing_version	        0.3.3
%define scim_version		1.4.5

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-chewing
Summary:	SCIM IMEngine module for chewing
Epoch:		1
Version:	%{version}
Release:	%mkrel 1
Group:		System/Internationalization
License:	GPL2+
URL:		https://chewing.csie.net/
Source0:	http://chewing.csie.net/download/scim/%name-%version.tar.bz2
Patch0:		scim-chewing-0.3.2-fix-linkage.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	libchewing >= 1:%{chewing_version}
Requires:	scim-client = %scim_api
BuildRequires:  libchewing-devel >= %{chewing_version}
BuildRequires:  scim-devel >= %{scim_version}
BuildRequires:  intltool gettext-devel
# compatibility
Obsoletes:	%mklibname %{name} 0

%description
Scim-chewing is an SCIM IMEngine module for chewing,
an intelligent Chinese phonetic input method.

%prep
%setup -q -n %name-%version
%patch0 -p0 -b .linkage

%build
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
