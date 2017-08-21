#!/usr/bin/env bash


#install pythonbrew
#from https://pypi.python.org/pypi/pythonbrew/
echo "install pythonbrew"
#该curl地址已经失效，可以使用pythonbrew-1.3.6来安装
#curl -kL http://xrl.us/pythonbrewinstall | bash



echo "config bashrc for pythonbrew"
[[ -s $HOME/.pythonbrew/etc/bashrc ]] && source $HOME/.pythonbrew/etc/bashrc

echo "install readline"
yum install readline readline-devel

pythonbrew install 2.7.4

#switch 用于永久生效 , use 用于临时生效（重入失效）
pythonbrew switch 2.7.4

echo "install pip"
curl https://bootstrap.pypa.io/get-pip.py -s | python

pip install sqlmap -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip install numpy -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip install scipy -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip install scikit-learn -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip install matplotlib==1.4.3 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip install panda -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com




