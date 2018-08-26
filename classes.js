class Item{
    constructor(name, link) {
        this.name = name;
        this.link = link;
    }
}


Item.prototype.toString = function() {
    return this.name + ", " + this.link;
}


class Bookshelf{
    constructor(item2tags, tag2items){
        this.item2tags = item2tags;
        this.tag2items = tag2items;
    }

}

Bookshelf.prototype.getItemsFromTag = function (tag) {
    if (! (tag in this.tag2items)){
        return [];
    }
    return this.tag2items[tag];
};
