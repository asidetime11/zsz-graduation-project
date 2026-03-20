module.exports={canOperate:(req)=>['reviewer','disburser'].includes(req.user.role)};
