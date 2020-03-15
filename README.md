# SETUP

### Installing pip

* Open the terminal
 

* Execute `curl https://bootstrap.pypa.io/get-pip.py -o ~/Downloads/get-pip.py`
or download 'get-pip.py' manually from `https://bootstrap.pypa.io/`.

* Run the installation: `python ~/Downloads/get-pip.py --user` on your local user,
pip will then be installed to ~/Library/Python/2.7/bin/pip

* Make sure `~/Library/Python/2.7/bin` is in your `$PATH`.
For `bash` users, edit the `PATH=` line in `~/.bashrc`/`~/.zshrc`/`~/.config/fish/config.fish` to append the local Python path;
ie. `PATH=$PATH:~/Library/Python/2.7/bin`
In Fish you need to write: `set -gx PATH ~/Library/Python/2.7/bin $PATH`

* Apply the changes, `source` `~/.bashrc`/`~/.zshrc`/`~/.config/fish/config.fish`.

### Installing pyYAML

* In order to convert a yaml file to html, the script needs a json file as input.
Therefore, we need you to install pyYaml.
Execute `python pip install pyyaml`.

---

# Getting started

* Put any .yaml-files into the `./src`-directory

* Execute `python convertSwaggerYamlToHtmlDoc.py'

* View all generated APIs in the `./targets`-directory