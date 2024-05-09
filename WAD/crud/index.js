const dbConnect=require('./mongodb')
const express=require('express')
const app=express();
app.use(express.json())

//get api
        app.get('/',async(req,res)=> {
        let result=await dbConnect();
        result=await result.find().toArray();
        res.send(result);
})
//POST API
        app.post('/',async(req,res)=>{
            let result=await dbConnect();
            result=await result.insertOne(req.body);
            res.send("data inserted sucessfully")
        })
//put api
        app.put('/:name',async(req,res)=>{
            let result=await dbConnect();
            result=await result.updateOne({name:req.params.name},{$set:req.body});
            res.send("data updated sucessfully")
        })
//delete api
        app.delete('/:name',async(req,res)=>{
            let result=await dbConnect();
            result=await result.deleteOne({name:req.params.name},{$set:req.body});
            res.send("data deleted successfully");
            
        })
app.listen(3000);