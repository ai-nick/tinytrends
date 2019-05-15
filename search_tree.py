import json

class GoldenTree(object):

    def __inti__(width, root, depth):
        self.width = width
        self.root_coord = root
        self.depth = depth
        self.num_dimens = len(self.root_coord)
         