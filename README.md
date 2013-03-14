ApacheTomcatRpmBuilder
==============

This project will allow people to build RPM packaged versions of Apache's Tomcat.

##Usage
1. from the root of the project run "gradle assemble"
2. A tarball can then be found in "build/distributions"
3. The rpm file can be found in "build/RPMS"

##Requirements
1. Java
2. Gradle
3. rpmbuild

##Future Enhancements
- Add auto download of latest tomcat
- Add runline arg support for different versions of tomcat
