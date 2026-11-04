from fastapi import FastAPI
import random
app = FastAPI() 
side_hustles = [
    "Blogging",     
    "Freelancing",
    "Consulting",
    "Online Courses",
    "Podcasting",
    "Affiliate Marketing",
    "Dropshipping",
    "E-commerce",
    "Social Media Marketing",
    "Web Development",
    "App Development",
    "Graphic Design",
    "Video Editing",]
money_making_ideas = [
    "Start a blog",
    "Start a YouTube channel",
    "Start a podcast",
    "Start a freelancing business",
    "Start a consulting business",
    "Start an online course",
    "Start an affiliate marketing business",
    "Start a dropshipping business",
    "Start an e-commerce business",
    "Start a social media marketing business",
    "Start a web development business",
    "Start an app development business",
    "Start a graphic design business"]
@app.get("/side_hustles")
def get_side_hustles():
    """Get a list of side hustles"""
    return {"side_hustles": random.choice(side_hustles)}
@app.get("/money_making_ideas")
def get_money_making_ideas():
    """Get a list of money making ideas"""
    return {"money_making_ideas": random.choice(money_making_ideas)}


