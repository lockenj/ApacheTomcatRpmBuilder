Name: ${name}
BuildArch: noarch
Version: ${version}
Release: ${release}
Summary: ${name}
Epoch: 0
License: Apache License version 2, http://www.apache.org/licenses
Group: apache.org
Source0: ${name}-${version}.tgz
Source1: ${name}
Requires: jdk >= 1.7


%description
Installs Apache Tomcat into /usr/${name}
	
	
%pre
getent group tomcat > /dev/null || groupadd -r tomcat
getent passwd tomcat > /dev/null || useradd -r -g tomcat tomcat


%post
chkconfig --add %{name}


%preun
if [[ "${1}" = "0" ]]; then
service %{name} stop > /dev/null 2>&1
chkconfig --del %{name}
fi
	
	
#Uncompress files to BUILD
%prep
%setup -c -q


#Configure/Compile files in BUILD
%install
rm -rf %{buildroot}
install --directory %{buildroot}/usr/${name}
install --directory %{buildroot}/usr/${name}/pid

install --directory %{buildroot}/var/${name}

install --directory %{buildroot}/etc/init.d/


install -m 755 ${name}-initscript %{buildroot}/etc/init.d/${name}
cp -rf ${name}-${version}/* %{buildroot}/usr/${name}/


#This will clean up after the software is packaged
%clean
#rm -rf %{buildroot}


#Specify files to be added to the RPM
%files
%defattr(-,tomcat,tomcat,-)

/usr/${name}
%config /usr/${name}/conf/*
/var/${name}

%attr(0755,root,root) /etc/init.d/${name}


#Specify the changes made since the last version
%changelog
* ${date} <${user}> ${version}
- Installs JDK 1.7+ 
- Installs Apache Tomcat into /usr/${name}
- Creates a tomcat user with password tomcat
- Makes ${name} a service