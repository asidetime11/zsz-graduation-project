class Review {
    static data = [
        { id: 1, merchant_id: 1, reviewer: 'ops', decision: 'pending' },
        { id: 2, merchant_id: 2, reviewer: 'ops', decision: 'approved' }
    ];

    static findByMerchantId(merchant_id) {
        return this.data.filter((r) => r.merchant_id === Number(merchant_id));
    }
}

module.exports = Review;
