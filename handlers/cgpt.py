"""
* @project       GeneralQBOT
* @author        XYCode <xycode-xyc@outlook.com>
* @date          1970-01-01 08:00:00
* @lastModified  2023-05-15 12:54:01
"""
import openai
import openai.error
import configs.config
import datetime
import asyncio
from typing import List, Dict

openai.api_key = configs.config.OPENAI_KEY

__all__ = ['generate_by_gpt']

async def generate_by_gpt(tips: str, data: str, other_message: List[Dict[str, str]] = []):
    try:
        data = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'system',
                    'content': f'现在是北京时间 {datetime.datetime.now()}'
                },
                {
                    'role': 'system',
                    'content': tips
                },
                {
                    'role': 'user',
                    'content': data
                },
                *other_message
            ]
        )
        
        return data.choices[0].message["content"]
    except: 
        # retry in 20 seconds
        asyncio.sleep(20)
        return await generate_by_gpt(tips, data, other_message)

async def generate_by_gpt_for_interview(message: List[Dict[str, str]] = []):
    try:
        data = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'system',
                    'content': f'现在是北京时间 {datetime.datetime.now()}'
                },
                *message
            ]
        )
        
        return data.choices[0].message["content"]
    except: 
        # retry in 20 seconds
        asyncio.sleep(20)
        return await generate_by_gpt_for_interview(message)