module.exports = {
    forms: [
        { id: 1, name: 'feedback', form_theme: 'light', script: 'return input;' }
    ],
    credentials: {
        api_secret: 'api-secret-in-env',
        db_password: 'db-pass-in-env'
    },
    submissions: [
        { id: 10, user_submission: '{"email":"a@b.com"}' }
    ],
    executionLogs: []
};
