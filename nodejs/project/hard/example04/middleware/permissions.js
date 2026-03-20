module.exports={withUser:(req,res,next)=>{req.user={id:req.headers['x-user-id']||'u401'};next();}};
