from bs4 import BeautifulSoup
import os


class Sadpanda:
    '''
    Explanation on what it does because I'll proably forget

        self.scrapper_file() function:

            Assuming all .html files are in the same folder, program will
            read each file and pass through Beautifulsoup using selected parser.

            After that it'll find all selected tags, iterate through them all
            to extract text in the tag and append in a list.

        self.writefile() function:

            Writes the contents of self.doujinlist into selected filename.

    '''

    def __init__(
        self,
        foldername=None,
        filename=None,
        tag=None,
        tagclass=None,
        tagclassname=None,
        encoding=None,
        parser=None

    ):

        self.foldername = foldername
        self.filename = filename
        self.tag = tag
        self.tagclass = tagclass
        self.tagclassname = tagclassname
        self.encoding = encoding
        self.parser = parser
        self.doujinlist = []

    def scrapper_file(self):
        '''
        Scraps tags from .html files

        '''

        for file in os.listdir(self.foldername):
            path = self.foldername + '\\' + file

            with open(path, encoding=self.encoding, errors='ignore') as page:
                soup = BeautifulSoup(page, self.parser)
            # silencing errors are not a good practice, this is a 'silver-tape' solution

                get_stuff = soup.find_all(
                    self.tag, attrs={self.tagclass: self.tagclassname}
                )
            # First of all, getting the right tag can be a pain because of
            # nesting in html. A PAIN.
            # Second, since this is far from being a fully funcional tag search
            # engine cof sorts, you can always modifiy attrs parameter to your
            # needs.
                for tag in get_stuff:
                    text = tag.get_text().strip()
                    tag_text_stuff = " ".join(text.split())

                    self.doujinlist.append(tag_text_stuff)

        return self.doujinlist

    def writefile(self):

        for item in self.doujinlist:

            save_path = self.foldername + '\\' + self.filename + '.txt'

            with open(save_path, 'a', encoding='utf8') as file:
                file.write(item + '\n')
