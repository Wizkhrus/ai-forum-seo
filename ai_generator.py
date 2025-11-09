import openai
import random
from database import db, Category, Thread, Post, generate_slug
from datetime import datetime, timedelta
import time

class AIForumGenerator:
    def __init__(self):
        openai.api_key = 'your-openai-api-key'
        
        # 120+ unique users database
        self.users = self.generate_users(120)
        self.topics_by_category = {
            'Технологии': ['AI', 'Blockchain', 'IoT', 'Cloud', 'Cybersecurity'],
            'Игры': ['Gaming', 'Esports', 'Indie', 'RPG', 'Multiplayer'],
            'Кино и сериалы': ['Movies', 'TV Shows', 'Streaming', 'Reviews'],
            'Наука': ['Physics', 'Biology', 'Astronomy', 'Research'],
            'Искусство': ['Art', 'Music', 'Design', 'Photography'],
            'Путешествия': ['Travel', 'Tourism', 'Adventures', 'Culture']
        }

    def generate_users(self, count):
        """Generate 120+ unique users"""
        first_names = ['Alex', 'John', 'Maria', 'Kate', 'James']
        last_names = ['Smith', 'Johnson', 'Brown', 'Davis']
        users = []
        for i in range(count):
            users.append({
                'name': f"{random.choice(first_names)}{random.randint(1,999)}",
                'style': random.choice(['expert', 'newbie', 'enthusiast'])
            })
        return users
    
    def generate_random_date(self):
        """Generate realistic date from 3 years ago"""
        days_ago = random.randint(1, 365*3)
        return datetime.utcnow() - timedelta(days=days_ago)
    
    def generate_ai_content(self, prompt):
        """Call OpenAI API for content"""
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[{'role': 'user', 'content': prompt}],
                max_tokens=500,
                temperature=0.8
            )
            return response.choices[0].message.content.strip()
        except:
            return 'Great discussion point! Looking forward to hearing more.'
    
    def generate_new_thread(self):
        """Create new forum thread with SEO-optimized content"""
        category = random.choice(Category.query.all())
        user = random.choice(self.users)
        topic = random.choice(self.topics_by_category.get(category.name, []))
        
        title = f"Discussion: {topic} in {category.name}"
        slug = generate_slug(title)
        content = self.generate_ai_content(f"Write forum post about {topic}")
        random_date = self.generate_random_date()
        
        thread = Thread(
            title=title,
            slug=slug,
            content=content,
            author_name=user['name'],
            category_id=category.id,
            created_at=random_date,
            last_activity=random_date,
            meta_title=f"Discuss {topic} - AI Forum",
            meta_description=f"Join discussion about {topic}"
        )
        db.session.add(thread)
        db.session.commit()
        return thread
    
    def generate_reply(self, thread):
        """Generate reply to thread"""
        user = random.choice(self.users)
        reply_date = thread.created_at + timedelta(hours=random.randint(1,48))
        content = self.generate_ai_content(f"Reply to: {thread.title}")
        
        post = Post(
            content=content,
            author_name=user['name'],
            thread_id=thread.id,
            created_at=reply_date
        )
        thread.post_count += 1
        thread.last_activity = reply_date
        db.session.add(post)
        db.session.commit()
