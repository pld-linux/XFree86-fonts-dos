Summary:	XFree86 misc fonts with DOS encodings
Summary(pl):	Fonty misc z DOS-owym kodowaniem
Name:		XFree86-fonts-dos
Version:	4.2.0
Release:	3
License:	Public Domain
Group:		Fonts
Source0:	XFree86-fonts-misc-%{version}.tar.bz2
# Source0-md5:	cbadfe4e784653b2795def646b905fb4
Source1:	%{name}-maps.tar.bz2
# Source1-md5:	edd71dbe130ae9ce39704ee2ee9e185e
Source2:	%{name}-Mazovia.map
BuildRequires:	XFree86-fonts-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This package contains fixed fonts with DOS encodings.
Fonts were taken from XFree86.

%description -l pl
Pakiet ten zawiera czcionki fixed z DOS-owym kodowaniem.
Fonty zosta³y wziête z dystrybucji XFree86.

%package -n XFree86-fonts-CP737
Summary:	Fixed CP737 fonts
Summary(pl):	Fonty rastrowe CP737
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP737
This package contains fixed fonts with CP737 encoding.

%description -n XFree86-fonts-CP737 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP737.

%package -n XFree86-fonts-CP775
Summary:	Fixed CP775 fonts
Summary(pl):	Fonty rastrowe CP775
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP775
This package contains fixed fonts with CP775 encoding.

%description -n XFree86-fonts-CP775 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP775.

%package -n XFree86-fonts-CP850
Summary:	Fixed CP850 fonts
Summary(pl):	Fonty rastrowe CP850
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP850
This package contains fixed fonts with CP850 encoding.

%description -n XFree86-fonts-CP850 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP850.

%package -n XFree86-fonts-CP852
Summary:	Fixed CP852 fonts
Summary(pl):	Fonty rastrowe CP852
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP852
This package contains fixed fonts with CP852 encoding.

%description -n XFree86-fonts-CP852 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP852.

%package -n XFree86-fonts-CP855
Summary:	Fixed CP855 fonts
Summary(pl):	Fonty rastrowe CP855
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP855
This package contains fixed fonts with CP855 encoding.

%description -n XFree86-fonts-CP855 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP855.

%package -n XFree86-fonts-CP857
Summary:	Fixed CP857 fonts
Summary(pl):	Fonty rastrowe CP857
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP857
This package contains fixed fonts with CP857 encoding.

%description -n XFree86-fonts-CP857 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP857.

%package -n XFree86-fonts-CP860
Summary:	Fixed CP860 fonts
Summary(pl):	Fonty rastrowe CP860
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP860
This package contains fixed fonts with CP860 encoding.

%description -n XFree86-fonts-CP860 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP860.

%package -n XFree86-fonts-CP861
Summary:	Fixed CP861 fonts
Summary(pl):	Fonty rastrowe CP861
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP861
This package contains fixed fonts with CP861 encoding.

%description -n XFree86-fonts-CP861 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP861.

%package -n XFree86-fonts-CP862
Summary:	Fixed CP862 fonts
Summary(pl):	Fonty rastrowe CP862
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP862
This package contains fixed fonts with CP862 encoding.

%description -n XFree86-fonts-CP862 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP862.

%package -n XFree86-fonts-CP863
Summary:	Fixed CP863 fonts
Summary(pl):	Fonty rastrowe CP863
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP863
This package contains fixed fonts with CP863 encoding.

%description -n XFree86-fonts-CP863 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP863.

%package -n XFree86-fonts-CP864
Summary:	Fixed CP864 fonts
Summary(pl):	Fonty rastrowe CP864
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP864
This package contains fixed fonts with CP864 encoding.

%description -n XFree86-fonts-CP864 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP864.

%package -n XFree86-fonts-CP865
Summary:	Fixed CP865 fonts
Summary(pl):	Fonty rastrowe CP865
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP865
This package contains fixed fonts with CP865 encoding.

%description -n XFree86-fonts-CP865 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP865.

%package -n XFree86-fonts-CP866
Summary:	Fixed CP866 fonts
Summary(pl):	Fonty rastrowe CP866
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP866
This package contains fixed fonts with CP866 encoding.

%description -n XFree86-fonts-CP866 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP866.

%package -n XFree86-fonts-CP869
Summary:	Fixed CP869 fonts
Summary(pl):	Fonty rastrowe CP869
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP869
This package contains fixed fonts with CP869 encoding.

%description -n XFree86-fonts-CP869 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP869.

%package -n XFree86-fonts-CP874
Summary:	Fixed CP874 fonts
Summary(pl):	Fonty rastrowe CP874
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-CP874
This package contains fixed fonts with CP874 encoding.

%description -n XFree86-fonts-CP874 -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem CP874.

%package -n XFree86-fonts-Mazovia
Summary:	Fixed Mazovia fonts
Summary(pl):	Fonty rastrowe Mazovia
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc

%description -n XFree86-fonts-Mazovia
This package contains fixed fonts with Mazovia encoding.

%description -n XFree86-fonts-Mazovia -l pl
Pakiet ten zawiera czcionki fixed z kodowaniem Mazovia.

%prep
%setup -q -n FONTS -a1
cp -f %{SOURCE2} map-Mazovia-0

%build
for i in *.bdf
do
	for j in 737 775 850 852 855 857 860 861 862 863 864 865 866 869 874
	do
		ucs2any $i map-CP$j-0 CP$j-0
		name=`basename $i .bdf`-CP$j-0
		bdftopcf -t $name.bdf | gzip -9 > $name.pcf.gz
		rm -f $name.bdf
	done
	ucs2any $i map-Mazovia-0 Mazovia-0
	name=`basename $i .bdf`-Mazovia-0
	bdftopcf -t $name.bdf | gzip -9 > $name.pcf.gz
	rm -f $name.bdf
done

%install
install -d $RPM_BUILD_ROOT%{_fontsdir}/misc
install *.pcf.gz $RPM_BUILD_ROOT%{_fontsdir}/misc

%post -n XFree86-fonts-CP737
fontpostinst misc

%postun -n XFree86-fonts-CP737
fontpostinst misc

%post -n XFree86-fonts-CP775
fontpostinst misc

%postun -n XFree86-fonts-CP775
fontpostinst misc

%post -n XFree86-fonts-CP850
fontpostinst misc

%postun -n XFree86-fonts-CP850
fontpostinst misc

%post -n XFree86-fonts-CP852
fontpostinst misc

%postun -n XFree86-fonts-CP852
fontpostinst misc

%post -n XFree86-fonts-CP855
fontpostinst misc

%postun -n XFree86-fonts-CP855
fontpostinst misc

%post -n XFree86-fonts-CP857
fontpostinst misc

%postun -n XFree86-fonts-CP857
fontpostinst misc

%post -n XFree86-fonts-CP860
fontpostinst misc

%postun -n XFree86-fonts-CP860
fontpostinst misc

%post -n XFree86-fonts-CP861
fontpostinst misc

%postun -n XFree86-fonts-CP861
fontpostinst misc

%post -n XFree86-fonts-CP862
fontpostinst misc

%postun -n XFree86-fonts-CP862
fontpostinst misc

%post -n XFree86-fonts-CP863
fontpostinst misc

%postun -n XFree86-fonts-CP863
fontpostinst misc

%post -n XFree86-fonts-CP864
fontpostinst misc

%postun -n XFree86-fonts-CP864
fontpostinst misc

%post -n XFree86-fonts-CP865
fontpostinst misc

%postun -n XFree86-fonts-CP865
fontpostinst misc

%post -n XFree86-fonts-CP866
fontpostinst misc

%postun -n XFree86-fonts-CP866
fontpostinst misc

%post -n XFree86-fonts-CP869
fontpostinst misc

%postun -n XFree86-fonts-CP869
fontpostinst misc

%post -n XFree86-fonts-CP874
fontpostinst misc

%postun -n XFree86-fonts-CP874
fontpostinst misc

%post -n XFree86-fonts-Mazovia
fontpostinst misc

%postun -n XFree86-fonts-Mazovia
fontpostinst misc

%clean
rm -rf $RPM_BUILD_ROOT

%files -n XFree86-fonts-CP737
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP737-0.pcf.gz

%files -n XFree86-fonts-CP775
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP775-0.pcf.gz

%files -n XFree86-fonts-CP850
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP850-0.pcf.gz

%files -n XFree86-fonts-CP852
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP852-0.pcf.gz

%files -n XFree86-fonts-CP855
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP855-0.pcf.gz

%files -n XFree86-fonts-CP857
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP857-0.pcf.gz

%files -n XFree86-fonts-CP860
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP860-0.pcf.gz

%files -n XFree86-fonts-CP861
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP861-0.pcf.gz

%files -n XFree86-fonts-CP862
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP862-0.pcf.gz

%files -n XFree86-fonts-CP863
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP863-0.pcf.gz

%files -n XFree86-fonts-CP864
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP864-0.pcf.gz

%files -n XFree86-fonts-CP865
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP865-0.pcf.gz

%files -n XFree86-fonts-CP866
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP866-0.pcf.gz

%files -n XFree86-fonts-CP869
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP869-0.pcf.gz

%files -n XFree86-fonts-CP874
%defattr(644,root,root,755)
%{_fontsdir}/misc/*CP874-0.pcf.gz

%files -n XFree86-fonts-Mazovia
%defattr(644,root,root,755)
%{_fontsdir}/misc/*Mazovia-0.pcf.gz
