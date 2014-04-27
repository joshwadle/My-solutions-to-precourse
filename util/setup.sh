## Setup a data science development mac mini box

# install xcode commandline tools

xcode-select --install

# homebrew
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

## Mac apps (uncomment any additional ones that you want)

brew tap phinze/cask
brew install brew-cask
# brew cask install google-chrome
# brew cask install firefox
# brew cask install mou
brew cask install iterm2
brew cask install xquartz
brew cask install virtualbox
brew cask install vagrant
brew cask install sublime-text
brew cask install pgadmin3

# To install Flux uncomment these lines

# cd /Applications
# wget https://justgetflux.com/mac/Flux.zip
# unzip Flux.zip
# rm Flux.zip

## mac packages
brew install wget
brew install postgres
brew install mongodb
brew install graphviz
brew install imagemagick

# python (Anaconda distribution)
wget http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-1.9.1-MacOSX-x86_64.sh
sh Anaconda-1.9.1-MacOSX-x86_64.sh

conda install --yes statsmodels
conda install --yes networkx

pip install pymc
pip install pymongo

# R
brew update
brew tap homebrew/science
brew install gfortran r