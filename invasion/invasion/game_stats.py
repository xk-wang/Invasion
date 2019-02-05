class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings=ai_settings
        self.reset_stats()
        #在任何情况下都不应该重置最高得分
        self.high_score=0
        #从文件读取历史最高分
        self.read_high_score()
        #游戏刚启动时处于非活跃状态
        self.game_active=False
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
    def save_high_score(self):
        """将最高得分存入文件"""
        with open('high_score.txt','w') as file_object:
            file_object.write(str(self.high_score))
    def read_high_score(self):
        """从文件中读入最高得分"""
        with open('high_score.txt') as file_object:
            contents=file_object.read()
        self.high_score=int(contents)
