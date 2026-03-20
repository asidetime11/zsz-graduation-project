class Post {
    static data = [
        { id: 1, user_id: 1, title: 'welcome', content: 'first post' }
    ];

    static findById(id) {
        return this.data.find((p) => p.id === Number(id));
    }

    static create(post) {
        const next = { id: this.data.length + 1, ...post };
        this.data.push(next);
        return next;
    }
}

module.exports = Post;
