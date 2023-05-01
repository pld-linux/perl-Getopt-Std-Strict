#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Getopt
%define		pnam	Std-Strict
Summary:	Getopt::Std::Strict
Name:		perl-Getopt-Std-Strict
Version:	1.01
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Getopt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a14a47cf9b336b24a113896dfb2f64f6
# generic URL, check or change before uncommenting
#URL:		https://metacpan.org/release/Getopt-Std-Strict
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nicer to use Getopt::Std variant.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Getopt/Std
%{perl_vendorlib}/Getopt/Std/Strict.pm
%{_mandir}/man3/Getopt::Std::Strict.3*
