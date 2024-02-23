
find . | grep -E "(\.ipynb_checkpoints)" | xargs rm -rf
find . | grep -E "(__pycache__|\.pyc$)" | xargs rm -rf

    
