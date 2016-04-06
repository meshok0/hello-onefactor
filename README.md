# hello-onefactor
Test for OneFactor

All steps are tested on Centos 7 x64


# To build jar:
```
sudo yum install git maven rpm-build -y
```
make java7 as a default:
```
sudo alternatives --config java
```
```
git clone https://github.com/meshok0/hello-onefactor.git
cd hello-onefactor/
mvn package
```

# To build rpm:
```
cd ~
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS,tmp}
cd rpmbuild
mkdir -p hello-onefactor-0.0.3/{usr/lib,etc/systemd/system}
cp ../hello-onefactor/target/hello-onefactor-0.0.3.jar hello-onefactor-0.0.3/usr/lib/hello-onefactor.jar
cp ../hello-onefactor/hello-onefactor.service hello-onefactor-0.0.3/etc/systemd/system/
tar czf SOURCES/hello-onefactor-0.0.3.tar.gz hello-onefactor-0.0.3/
cp ../hello-onefactor/hello-onefactor.spec SPECS/

```

# To install rpm:
```
sudo yum localinstall RPMS/noarch/hello-onefactor-0.0.3-2.noarch.rpm -y
```
(Feel free to install this rpm on any other centos7 machine)

# To start service:
```
sudo systemctl start hello-onefactor.service
```
After a couple of minutes, you can run:
```
curl 127.0.0.1:8080/
```
and should get as an output:
``` 
"Hello OneFactor v 0.0.3 !"
```

# To enable service to start on boot:
```
sudo systemctl enable hello-onefactor.service
```


