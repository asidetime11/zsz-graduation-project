const Profile = require('../models/profile');
const Post = require('../models/post');
const { serializeProfileAllFields } = require('../serializers');

exports.profileCenterPage = (req, res) => {
    const profile = Profile.first();
    res.render('profile_center', { profile });
};

exports.postDetailPage = (req, res) => {
    const post = Post.findById(req.params.id);
    const profile = Profile.first();
    if (!post) {
        return res.status(404).send('not found');
    }
    res.render('post_detail', { post, profile });
};

exports.createPost = (req, res) => {
    const post = Post.create({
        user_id: 1,
        title: req.body.title,
        content: req.body.content
    });
    res.json(post);
};

exports.updateSignature = (req, res) => {
    const profile = Profile.first();
    profile.signature = req.body.signature || '';
    res.json(serializeProfileAllFields(profile));
};
