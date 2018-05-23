# This file is auto-generated, please don't modify it directly.
# Modify source xls file and use model_gen to regenerate again.
#
# Last generate time: 2018-05-23 13:11:16

from django.db import models

# Description: 玩法静态表
# Group: CatLogicStatic
class GameStatic(models.Model):
	# Description: 玩法类型
	# Type: enum(EnumGameType,Drier(吹风机),Laser(激光笔),Feed(喂食),PutUp(托起),Stroke(抚摸),Click(点击))
	# Unique: False, Required: True
	# Server: True, Client: True
	GameType = models.IntegerField(default=0)

	# Description: 玩法图标资源
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	GameIcon = models.CharField(max_length=255)

	# Description: 玩法资源
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	GameResource = models.CharField(max_length=255, null=True, blank=True)

	# Description: 玩法描述
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	GameDescription = models.CharField(max_length=255, null=True, blank=True)

	# Description: 最小使用饱食度
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	MinHungryNum = models.IntegerField(default=0)

	# Description: 增加心情值间隔（秒）
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HappyPerTime = models.IntegerField(default=0)

	# Description: 每次增加心情值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	AddHappyNum = models.IntegerField(default=0)

	# Description: 每日可获得心情值上限
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	MaxHappyNum = models.IntegerField(default=0)

	# Description: 增加经验值间隔（秒）
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	ExpPerTime = models.IntegerField(default=0)

	# Description: 每次增加经验值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	AddExpNum = models.IntegerField(default=0)

	# Description: 每日可获得经验值上限
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	MaxExpNum = models.IntegerField(default=0)

	# Description: 增加金币间隔（秒）
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	GoldPerTime = models.IntegerField(default=0)

	# Description: 每次增加金币
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	AddGoldNum = models.IntegerField(default=0)

	# Description: 每日可获得金币上限
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	MaxGoldNum = models.IntegerField(default=0)

	# Description: 预留参数Json 根据玩法的不同参数不同
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	LogicGameParam = models.CharField(max_length=255)

	def __str__(self):
		return 'GameStatic: ' + str(self.id)

# Description: 角色动态表
# Group: ActorLogicMobile
class ActorMobile(models.Model):
	# Description: 角色名字
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	ActorName = models.CharField(max_length=255)

	# Description: 金币
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	Coin = models.IntegerField(default=0)

	# Description: 薄荷金币
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	Mint = models.IntegerField(default=0)

	# Description: 经验值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	Exp = models.IntegerField(default=0)

	# Description: 等级
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	Level = models.IntegerField(default=0)

	# Description: 开启时间
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	BeginDay = models.IntegerField(default=0)

	# Description: 吹风机增加经验值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	GameLogicDrierAddExp = models.IntegerField(default=0)

	# Description: 激光笔增加经验值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	GameLogicLaserAddExp = models.IntegerField(default=0)

	# Description: 吹风机增加心情值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	GameLogicDrierAddHappy = models.IntegerField(default=0)

	# Description: 激光笔增加心情值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	GameLogicLaserAddHappy = models.IntegerField(default=0)

	# Description: 每日任务开始时间
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	DailyTaskGetTime = models.CharField(max_length=255)

	# Description: 购买药瓶记录
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	BuyMedicineNum = models.IntegerField(default=0)

	# Description: 角色唯一ID
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	ActorID = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return 'ActorMobile: ' + str(self.id)

# Description: 猫拥有礼物表
# Group: ActorLogicMobile
class GiftMobile(models.Model):
	# Description: 金币数
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	CoinNum = models.IntegerField(default=0)

	# Description: 卡片id
	# Type: bool
	# Unique: False, Required: True
	# Server: True, Client: True
	CardStaticID = models.BooleanField(default=False)

	def __str__(self):
		return 'GiftMobile: ' + str(self.id)

# Description: 食物静态表
# Group: CatLogicStatic
class FoodStatic(models.Model):
	# Description: 猫食物类型
	# Type: enum(EnumFoodType,CatFood(猫粮),GreenFood(蔬菜),Banana(香蕉),Fish(鱼干),Cheese(奶酪),CatCan(猫罐头),MedicineOne(一号药瓶),MedicineTwo(二号药瓶))
	# Unique: False, Required: True
	# Server: True, Client: True
	FoodType = models.IntegerField(default=0)

	# Description: 解锁猫年龄
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	UnlockCatAge = models.IntegerField(default=0, null=True, blank=True)

	# Description: 解锁金币
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	UnlockCoin = models.IntegerField(default=0, null=True, blank=True)

	# Description: 分享解锁
	# Type: bool
	# Unique: False, Required: False
	# Server: True, Client: True
	UnlockEnjoy = models.BooleanField(default=False)

	# Description: 花费金币
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	Coin = models.IntegerField(default=0)

	# Description: 花费薄荷
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	Mint = models.IntegerField(default=0)

	# Description: 增加饱食度
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HungryPoint = models.IntegerField(default=0)

	# Description: 增加愉悦度
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HappyPoint = models.IntegerField(default=0)

	# Description: 增加经验值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	LevelPoint = models.IntegerField(default=0)

	# Description: 增加健康值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HealthPoint = models.IntegerField(default=0)

	# Description: 食物对应图片名字
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	FoodIconName = models.CharField(max_length=255)

	def __str__(self):
		return 'FoodStatic: ' + str(self.id)

# Description: 任务事件动态表
# Group: ActorLogicMobile
class TaskEventMobile(models.Model):
	# Description: 事件类型
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	EventType = models.IntegerField(default=0)

	# Description: 事件参数
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	EventParam = models.IntegerField(default=0)

	def __str__(self):
		return 'TaskEventMobile: ' + str(self.id)

# Description: 任务动态表
# Group: ActorLogicMobile
class TaskOwnMobile(models.Model):
	# Description: 任务类型
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	TaskType = models.IntegerField(default=0)

	# Description: 任务ID
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	TaskID = models.IntegerField(default=0)

	# Description: 任务完成标记
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	TaskFinish = models.IntegerField(default=0)

	def __str__(self):
		return 'TaskOwnMobile: ' + str(self.id)

# Description: 猫静态表
# Group: CatLogicStatic
class CatStatic(models.Model):
	# Description: 猫类型
	# Type: enum(EnumCatType,MiniCat(幼年期),YoungCat(成长期))
	# Unique: False, Required: True
	# Server: True, Client: True
	CatType = models.IntegerField(default=0)

	# Description: 猫资源
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CatBaseResource = models.CharField(max_length=255)

	# Description: None
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CatWholeBodyMeshName = models.CharField(max_length=255)

	# Description: None
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CatBodyNotEarMeshName = models.CharField(max_length=255)

	# Description: 猫部分资源
	# Type: array(string)
	# Unique: False, Required: True
	# Server: True, Client: True
	CatPartResource = models.TextField()

	# Description: 待机行为参数
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	IdleBehaviorParam = models.CharField(max_length=255, null=True, blank=True)

	# Description: 喂食行为参数
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	FeedBehaviorParam = models.CharField(max_length=255, null=True, blank=True)

	# Description: 激光笔行为参数
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	LazerBehaviorParam = models.CharField(max_length=255, null=True, blank=True)

	# Description: 吹风机行为参数
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	DryerBehaviorParam = models.CharField(max_length=255, null=True, blank=True)

	# Description: 健康值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HealthPoint = models.IntegerField(default=0)

	# Description: 健康值最大值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HealthMaxPoint = models.IntegerField(default=0)

	# Description: 体重
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	WeightPoint = models.IntegerField(default=0)

	# Description: 体重最大值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	WeightMaxPoint = models.IntegerField(default=0)

	# Description: 初始化经验值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	ExpPoint = models.IntegerField(default=0)

	# Description: 经验增加时间间隔（秒）
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	ExpAddTimeSpan = models.IntegerField(default=0)

	# Description: 经验每时间间隔增加数值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	ExpAddNum = models.IntegerField(default=0)

	# Description: 心情值增加健康值最小值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HappyPointAddHealthPoint = models.IntegerField(default=0)

	# Description: 饱食度增加心情值最小值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HungryPointAddHealthPoint = models.IntegerField(default=0)

	# Description: 心情值初始值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HappyInitialPoint = models.IntegerField(default=0)

	# Description: 心情值最大值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HappyMaxPoint = models.IntegerField(default=0)

	# Description: 饱食度初始值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HungryInitialPoint = models.IntegerField(default=0)

	# Description: 饱食度最大值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HungryMaxPoint = models.IntegerField(default=0)

	# Description: 成长点
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	LevelPoint = models.IntegerField(default=0)

	# Description: 最大成长点
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	MaxLevelPoint = models.IntegerField(default=0, null=True, blank=True)

	# Description: 下一个等级猫
	# Type: id(CatStatic)
	# Unique: False, Required: False
	# Server: True, Client: True
	NexLevelID = models.ForeignKey('CatStatic', on_delete=models.CASCADE, related_name='PrevLevelID', null=True, blank=True)

	def __str__(self):
		return 'CatStatic: ' + str(self.id)

# Description: 猫经验增加静态表
# Group: CatLogicStatic
class ExpAddStatic(models.Model):
	# Description: 等级值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	LevelPoint = models.IntegerField(default=0)

	# Description: 等级需要的经验值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	ExpPoint = models.IntegerField(default=0)

	def __str__(self):
		return 'ExpAddStatic: ' + str(self.id)

# Description: 猫健康对应体重静态表
# Group: CatLogicStatic
class WeightAddStatic(models.Model):
	# Description: 健康值0对应的体重值x1000
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	WeightNumHealthZeroPoint = models.IntegerField(default=0)

	# Description: 健康值1对应的体重值x1000
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	WeightNumHealthOnePoint = models.IntegerField(default=0)

	# Description: 健康值2对应的体重值x1000
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	WeightNumHealthTwoPoint = models.IntegerField(default=0)

	# Description: 健康值3对应的体重值x1000
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	WeightNumHealthThreePoint = models.IntegerField(default=0)

	# Description: 健康值4对应的体重值x1000
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	WeightNumHealthFourPoint = models.IntegerField(default=0)

	# Description: 健康值5对应的体重值x1000
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	WeightNumHealthFivePoint = models.IntegerField(default=0)

	def __str__(self):
		return 'WeightAddStatic: ' + str(self.id)

# Description: 猫音效表
# Group: CatLogicStatic
class CatSoundStatic(models.Model):
	# Description: 猫ID
	# Type: array(int)
	# Unique: False, Required: True
	# Server: True, Client: True
	CatID = models.TextField()

	# Description: 动画名称
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	AnimationName = models.CharField(max_length=255)

	# Description: 音效名称
	# Type: array(string)
	# Unique: False, Required: True
	# Server: True, Client: True
	SoundNameArray = models.TextField()

	def __str__(self):
		return 'CatSoundStatic: ' + str(self.id)

# Description: 音效静态表
# Group: InitializeStatic
class AudioStatic(models.Model):
	# Description: None
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	Describe = models.CharField(max_length=255, null=True, blank=True)

	# Description: 音效类型
	# Type: enum(AudioType, Auido2D(2D音效), Audio3D(3D音效))
	# Unique: False, Required: True
	# Server: True, Client: True
	AudioType = models.IntegerField(default=0)

	# Description: 音效名字
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	AudioName = models.CharField(max_length=255)

	# Description: 音效音量
	# Type: float
	# Unique: False, Required: True
	# Server: True, Client: True
	AudioVolumn = models.FloatField(default=0)

	# Description: 音效循环
	# Type: bool
	# Unique: False, Required: True
	# Server: True, Client: True
	AudioLoopParamName = models.BooleanField(default=False)

	# Description: 3D音效最小距离
	# Type: float
	# Unique: False, Required: False
	# Server: True, Client: True
	Audio3DMinDistance = models.FloatField(default=0, null=True, blank=True)

	# Description: 3D音效最大距离
	# Type: float
	# Unique: False, Required: False
	# Server: True, Client: True
	Audio3DMaxDistance = models.FloatField(default=0, null=True, blank=True)

	def __str__(self):
		return 'AudioStatic: ' + str(self.id)

# Description: 金币薄荷商店
# Group: ShopStaticGroup
class GoldMintShopStatic(models.Model):
	# Description: 商店物品类型
	# Type: enum(EnumShopItemType,Coin(金币),Mint(薄荷),Prop_Grass(道具猫草),Prop_Toy(道具玩具))
	# Unique: False, Required: True
	# Server: True, Client: True
	ShopItemType = models.IntegerField(default=0)

	# Description: 标签类型
	# Type: enum(EnumShopItemTagType,Hot(热卖),Promotion(促销))
	# Unique: False, Required: False
	# Server: True, Client: True
	ShopItemTagType = models.IntegerField(default=0, null=True, blank=True)

	# Description: 价格
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	ShopItemPrice = models.IntegerField(default=0, null=True, blank=True)

	# Description: 物品id
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	ProductID = models.CharField(max_length=255)

	# Description: 数量
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	ShopItemNum = models.IntegerField(default=0, null=True, blank=True)

	# Description: 排序
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	ShopItemSequence = models.IntegerField(default=0, null=True, blank=True)

	# Description: 中文价格
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	ShopItemCNPrice = models.CharField(max_length=255, null=True, blank=True)

	# Description: 英文价格
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	ShopItemENPrice = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return 'GoldMintShopStatic: ' + str(self.id)

# Description: 道具商店
# Group: ShopStaticGroup
class PropShopStatic(models.Model):
	# Description: 商店物品类型
	# Type: EnumShopItemType
	# Unique: False, Required: True
	# Server: True, Client: True
	ShopItemType = models.IntegerField(default=0)

	# Description: 商店物品ID
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	ShopItemID = models.IntegerField(default=0)

	# Description: 价格
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	ShopItemPrice = models.IntegerField(default=0)

	# Description: 数量
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	ShopItemNum = models.IntegerField(default=0)

	# Description: 排序
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	ShopItemSequence = models.IntegerField(default=0)

	def __str__(self):
		return 'PropShopStatic: ' + str(self.id)

# Description: 新手引导静态表
# Group: UserGuideStaticGroup
class UserGuideStatic(models.Model):
	# Description: 用户引导条件
	# Type: array(id(UserGuideConditionStatic))
	# Unique: False, Required: True
	# Server: True, Client: True
	UserGuideCondition = models.ManyToManyField('UserGuideConditionStatic', related_name='UserGuideConditionRelated')

	# Description: 用户引导事件
	# Type: array(id(UserGuideEventStatic))
	# Unique: False, Required: True
	# Server: True, Client: True
	UserGuideEvent = models.ManyToManyField('UserGuideEventStatic', related_name='UserGuideEventRelated')

	# Description: 下一个引导列表
	# Type: array(id(UserGuideStatic))
	# Unique: False, Required: True
	# Server: True, Client: True
	NextGuideID = models.ManyToManyField('UserGuideStatic', related_name='PrevGuideID')

	def __str__(self):
		return 'UserGuideStatic: ' + str(self.id)

# Description: 新手引导静态条件表
# Group: UserGuideStaticGroup
class UserGuideConditionStatic(models.Model):
	# Description: 条件类型
	# Type: enum(EnumUserGuideConditionType,OpenView(打开界面),Property(属性判断),ViewBtnPress(按钮摁下))
	# Unique: False, Required: True
	# Server: True, Client: True
	UserGuideConditionType = models.IntegerField(default=0)

	# Description: 条件参数
	# Type: array(string)
	# Unique: False, Required: True
	# Server: True, Client: True
	ConditionParam = models.TextField()

	def __str__(self):
		return 'UserGuideConditionStatic: ' + str(self.id)

# Description: 新手引导事件静态表
# Group: UserGuideStaticGroup
class UserGuideEventStatic(models.Model):
	# Description: 事件类型
	# Type: enum(EnumUserGuideEventType,MoveToButton(移动按钮事件),TextShow(文本显示),AIAction(AI行为),SetGuideFinish(设置引导结束))
	# Unique: False, Required: True
	# Server: True, Client: True
	UserGuideEventType = models.IntegerField(default=0)

	# Description: 条件参数
	# Type: array(string)
	# Unique: False, Required: True
	# Server: True, Client: True
	EventParam = models.TextField()

	# Description: 下一个触发的事件列表
	# Type: array(id(UserGuideEventStatic))
	# Unique: False, Required: True
	# Server: True, Client: True
	NextGuideEventIDArray = models.ManyToManyField('UserGuideEventStatic', related_name='PrevGuideEventIDArray')

	def __str__(self):
		return 'UserGuideEventStatic: ' + str(self.id)

# Description: 猫经验升级静态表
# Group: CatLogicStatic
class CatLevelStatic(models.Model):
	# Description: 等级
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	LevelNum = models.IntegerField(default=0)

	# Description: 经验
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	ExpNum = models.IntegerField(default=0)

	def __str__(self):
		return 'CatLevelStatic: ' + str(self.id)

# Description: 猫拥有动态表
# Group: CatLogicMobile
class CatOwnMobile(models.Model):
	# Description: 拥有类型
	# Type: enum(EnumOwnItemType,Food(粮食),Costume(服装),Grass(猫草),Toy(玩具),Card(卡片))
	# Unique: False, Required: True
	# Server: True, Client: True
	OwnItemType = models.IntegerField(default=0)

	# Description: 物品ID
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	OwnItemID = models.IntegerField(default=0)

	# Description: 是否装备
	# Type: bool
	# Unique: False, Required: True
	# Server: True, Client: True
	EuipOrNot = models.BooleanField(default=False)

	# Description: 物品数量
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	OwnNum = models.IntegerField(default=0)

	# Description: 属于猫的ID
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	CatID = models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return 'CatOwnMobile: ' + str(self.id)

# Description: 猫动态表
# Group: CatLogicMobile
class CatMobile(models.Model):
	# Description: None
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	CatStaticID = models.IntegerField(default=0)

	# Description: 猫的名字
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CatName = models.CharField(max_length=255)

	# Description: 猫的年龄
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	CatAge = models.IntegerField(default=0)

	# Description: 等级
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	LevelPoint = models.IntegerField(default=0)

	# Description: 心情值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HappyPoint = models.IntegerField(default=0)

	# Description: 饱食度
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HungryPoint = models.IntegerField(default=0)

	# Description: 健康值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	HealthPoint = models.IntegerField(default=0)

	# Description: 经验值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	ExpPoint = models.IntegerField(default=0)

	# Description: 体重值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	WeightPoint = models.IntegerField(default=0)

	# Description: 猫的生日
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CatBirthday = models.CharField(max_length=255)

	def __str__(self):
		return 'CatMobile: ' + str(self.id)

# Description: 多国语言静态表
# Group: InitializeStatic
class LanguageStatic(models.Model):
	# Description: 英文
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	LanguageEngInfo = models.CharField(max_length=255, null=True, blank=True)

	# Description: 中文
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	LanguageChnInfo = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return 'LanguageStatic: ' + str(self.id)

# Description: 对话框静态表
# Group: InitializeStatic
class DialogStatic(models.Model):
	# Description: 对话框类型
	# Type: enum(EnumDialogType,Hat(帽子),Neckcloth(领带),Glass(眼镜),CostumeClearAllFashionDialog(换衣间时装清除))
	# Unique: False, Required: True
	# Server: True, Client: True
	DialogType = models.IntegerField(default=0)

	# Description: 标题
	# Type: id(LanguageStatic)
	# Unique: False, Required: True
	# Server: True, Client: True
	DialogTitle = models.ForeignKey('LanguageStatic', on_delete=models.CASCADE, related_name='DialogTitleRelated')

	# Description: 内容
	# Type: id(LanguageStatic)
	# Unique: False, Required: True
	# Server: True, Client: True
	DialogInfo = models.ForeignKey('LanguageStatic', on_delete=models.CASCADE, related_name='DialogInfoRelated')

	def __str__(self):
		return 'DialogStatic: ' + str(self.id)

# Description: 道具静态表
# Group: CatLogicStatic
class PropStatic(models.Model):
	# Description: 道具类型
	# Type: enum(EnumPropType,Grass(猫草),Toy(玩具))
	# Unique: False, Required: True
	# Server: True, Client: True
	PropType = models.IntegerField(default=0)

	# Description: 道具名字
	# Type: id(LanguageStatic)
	# Unique: False, Required: True
	# Server: True, Client: True
	PropName = models.ForeignKey('LanguageStatic', on_delete=models.CASCADE, related_name='PropNameRelated')

	# Description: 道具描述
	# Type: id(LanguageStatic)
	# Unique: False, Required: True
	# Server: True, Client: True
	PropDescirption = models.ForeignKey('LanguageStatic', on_delete=models.CASCADE, related_name='PropDescirptionRelated')

	# Description: 道具图标
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	PropIcon = models.CharField(max_length=255)

	# Description: 道具叠加数
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	PropMaxNum = models.IntegerField(default=0)

	# Description: 花费金币
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	Coin = models.IntegerField(default=0)

	# Description: 花费薄荷
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	Mint = models.IntegerField(default=0)

	# Description: 最小时间
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	TimeMin = models.IntegerField(default=0)

	# Description: 最大时间
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	TimeMax = models.IntegerField(default=0)

	# Description: 最小金币
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	GoldMin = models.IntegerField(default=0)

	# Description: 最大金币
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	GoldMax = models.IntegerField(default=0)

	def __str__(self):
		return 'PropStatic: ' + str(self.id)

# Description: 每日任务静态表
# Group: TaskStaticGroup
class DailyTaskStatic(models.Model):
	# Description: 每日任务名称
	# Type: id(LanguageStatic)
	# Unique: False, Required: False
	# Server: True, Client: True
	DailyTaskName = models.ForeignKey('LanguageStatic', on_delete=models.CASCADE, related_name='DailyTaskNameRelated', null=True, blank=True)

	# Description: 出现概率（1-100）
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	DailyTaskProbability = models.IntegerField(default=0)

	# Description: 事件类型
	# Type: enum(EnumEventType,Stroke(抚摸),Feed(喂食),Enjoy(分享))
	# Unique: False, Required: True
	# Server: True, Client: True
	EventType = models.IntegerField(default=0)

	# Description: 事件完成次数
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	TaskEventNum = models.IntegerField(default=0)

	def __str__(self):
		return 'DailyTaskStatic: ' + str(self.id)

# Description: 每日任务静态表
# Group: TaskStaticGroup
class DailyTaskRewardStatic(models.Model):
	# Description: 天数
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	DayNum = models.IntegerField(default=0, null=True, blank=True)

	# Description: 奖励经验
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	CreditExp = models.IntegerField(default=0, null=True, blank=True)

	# Description: 奖励金币
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	CreditCoin = models.IntegerField(default=0, null=True, blank=True)

	# Description: 奖励薄荷
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	CreditMint = models.IntegerField(default=0, null=True, blank=True)

	# Description: 奖励道具
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	CreditPropID = models.IntegerField(default=0, null=True, blank=True)

	# Description: 奖励服装
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	CreditCostum = models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return 'DailyTaskRewardStatic: ' + str(self.id)

# Description: 七日签到静态表
# Group: TaskStaticGroup
class SevenDaySignStatic(models.Model):
	# Description: 第几天
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	DayNum = models.IntegerField(default=0)

	# Description: 奖励金币
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	AddCoin = models.IntegerField(default=0, null=True, blank=True)

	# Description: 奖励道具
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	AddPropID = models.IntegerField(default=0, null=True, blank=True)

	def __str__(self):
		return 'SevenDaySignStatic: ' + str(self.id)

# Description: 猫路线静态表
# Group: CardStaticGroup
class CatPathStatic(models.Model):
	# Description: 激活条件-猫草（ID可复选）
	# Type: array(id(PropStatic))
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerGrassID = models.ManyToManyField('PropStatic', related_name='TriggerGrassIDRelated', null=True, blank=True)

	# Description: 激活条件-最小健康值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	TriggerHealthPointMin = models.IntegerField(default=0)

	# Description: 激活条件-最大健康值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	TriggerHealthPointMax = models.IntegerField(default=0)

	# Description: 激活条件—猫的最小等级
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	TriggerCatLevelMin = models.IntegerField(default=0)

	# Description: 激活条件—猫的最大等级
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	TriggerCatLevelMax = models.IntegerField(default=0)

	# Description: 激活基础卡包
	# Type: array(id(CardBagStatic))
	# Unique: False, Required: True
	# Server: True, Client: True
	TriggerBaseCardBagID = models.ManyToManyField('CardBagStatic', related_name='TriggerBaseCardBagIDRelated')

	# Description: 激活稀有卡包
	# Type: array(id(CardBagStatic))
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerRareCardBagID = models.ManyToManyField('CardBagStatic', related_name='TriggerRareCardBagIDRelated', null=True, blank=True)

	# Description: 激活玩具卡包 玩具id 1
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardConditionID1 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包1概率
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerCardProbability1 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包 1
	# Type: id(CardBagStatic)
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardBagID1 = models.ForeignKey('CardBagStatic', on_delete=models.CASCADE, related_name='TriggerToyCardBagID1Related', null=True, blank=True)

	# Description: 激活玩具卡包 玩具id 2
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardConditionID2 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包2概率
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerCardProbability2 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包 2
	# Type: id(CardBagStatic)
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardBagID2 = models.ForeignKey('CardBagStatic', on_delete=models.CASCADE, related_name='TriggerToyCardBagID2Related', null=True, blank=True)

	# Description: 激活玩具卡包 玩具id 3
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardConditionID3 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包3概率
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerCardProbability3 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包 3
	# Type: id(CardBagStatic)
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardBagID3 = models.ForeignKey('CardBagStatic', on_delete=models.CASCADE, related_name='TriggerToyCardBagID3Related', null=True, blank=True)

	# Description: 激活玩具卡包 玩具id 4
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardConditionID4 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包4概率
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerCardProbability4 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包 4
	# Type: id(CardBagStatic)
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardBagID4 = models.ForeignKey('CardBagStatic', on_delete=models.CASCADE, related_name='TriggerToyCardBagID4Related', null=True, blank=True)

	# Description: 激活玩具卡包 玩具id 5
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardConditionID5 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包5概率
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerCardProbability5 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包 5
	# Type: id(CardBagStatic)
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardBagID5 = models.ForeignKey('CardBagStatic', on_delete=models.CASCADE, related_name='TriggerToyCardBagID5Related', null=True, blank=True)

	# Description: 激活玩具卡包 玩具id 6
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardConditionID6 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包6概率
	# Type: int
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerCardProbability6 = models.IntegerField(default=0, null=True, blank=True)

	# Description: 激活玩具卡包 6
	# Type: id(CardBagStatic)
	# Unique: False, Required: False
	# Server: True, Client: True
	TriggerToyCardBagID6 = models.ForeignKey('CardBagStatic', on_delete=models.CASCADE, related_name='TriggerToyCardBagID6Related', null=True, blank=True)

	def __str__(self):
		return 'CatPathStatic: ' + str(self.id)

# Description: 卡包静态表
# Group: CardStaticGroup
class CardBagStatic(models.Model):
	# Description: 卡包类型
	# Type: enum(EnumCardBagType,Common(普通),Rare(稀有),Toy(玩具))
	# Unique: False, Required: True
	# Server: True, Client: True
	CardBagType = models.IntegerField(default=0)

	# Description: 卡包权重
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	CardBagProbability = models.IntegerField(default=0)

	def __str__(self):
		return 'CardBagStatic: ' + str(self.id)

# Description: 卡片静态表
# Group: CardStaticGroup
class CardStatic(models.Model):
	# Description: 隶属卡包ID
	# Type: id(CardBagStatic)
	# Unique: False, Required: True
	# Server: True, Client: True
	CardBagID = models.ForeignKey('CardBagStatic', on_delete=models.CASCADE, related_name='CardBagIDRelated')

	# Description: 卡权重
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	CardProbability = models.IntegerField(default=0)

	# Description: 卡片资源
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CardRes = models.CharField(max_length=255)

	# Description: 卡片星级
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	CardStar = models.IntegerField(default=0)

	# Description: 回收金币
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	RecycleCoin = models.IntegerField(default=0)

	def __str__(self):
		return 'CardStatic: ' + str(self.id)

# Description: 常量静态表
# Group: InitializeStatic
class ConstStatic(models.Model):
	# Description: 猫获取经验触发时间间隔(小时)
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	CatTriggerTime = models.IntegerField(default=0)

	# Description: 最多收集卡片数量
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	MaxRestoreCardNum = models.IntegerField(default=0)

	# Description: ar房间背景音乐
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	BgSoundName_ARRoom = models.CharField(max_length=255)

	# Description: 3D房间背景音乐
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	BgSoundName_3DRoom = models.CharField(max_length=255)

	# Description: 试衣间背景音乐
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	BgSoundName_FittingRoom = models.CharField(max_length=255)

	# Description: 获得金币音效
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CommonSound_GetCoin = models.CharField(max_length=255)

	# Description: 获得卡片音效
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CommonSound_GetCard = models.CharField(max_length=255)

	# Description: 打开界面音效
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CommonSound_OpenView = models.CharField(max_length=255)

	# Description: 获得超级卡片音效
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CommonSound_GetSunperCard = models.CharField(max_length=255)

	def __str__(self):
		return 'ConstStatic: ' + str(self.id)

# Description: 时装静态表
# Group: CatLogicStatic
class CostumeStatic(models.Model):
	# Description: 时装类型
	# Type: enum(EnumCostumeType,Hat(帽子),Neckcloth(领带),Glass(眼镜),Hair(毛色))
	# Unique: False, Required: True
	# Server: True, Client: True
	CostumeType = models.IntegerField(default=0)

	# Description: 是否需要耳朵
	# Type: bool
	# Unique: False, Required: True
	# Server: True, Client: True
	BodyWithEar = models.BooleanField(default=False)

	# Description: 服装资源
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CostumeResource = models.CharField(max_length=255)

	# Description: 服装挂点
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CostumeHangPoint = models.CharField(max_length=255)

	# Description: 服装名字
	# Type: id(LanguageStatic)
	# Unique: False, Required: True
	# Server: True, Client: True
	CostumeName = models.ForeignKey('LanguageStatic', on_delete=models.CASCADE, related_name='CostumeNameRelated')

	# Description: 服装魅力值
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	CostumeCharm = models.IntegerField(default=0)

	# Description: 金币价格
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	CostumePrice = models.IntegerField(default=0)

	# Description: 薄荷价格
	# Type: int
	# Unique: False, Required: True
	# Server: True, Client: True
	MintPrice = models.IntegerField(default=0)

	# Description: 服装对应图片名字
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	CostumeIconName = models.CharField(max_length=255)

	# Description: 服装对应猫咪ID
	# Type: array(id(CatStatic))
	# Unique: False, Required: True
	# Server: True, Client: True
	CostumeMatchedCat = models.ManyToManyField('CatStatic', related_name='CostumeMatchedCatRelated')

	def __str__(self):
		return 'CostumeStatic: ' + str(self.id)

# Description: 动画静态表
# Group: InitializeStatic
class AnimationStatic(models.Model):
	# Description: 动画名字
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	AnimationName = models.CharField(max_length=255)

	# Description: 动画状态名字
	# Type: string
	# Unique: False, Required: True
	# Server: True, Client: True
	AnimationStateName = models.CharField(max_length=255)

	# Description: 动画参数名字
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	AnimationParamName = models.CharField(max_length=255, null=True, blank=True)

	# Description: 动画参数数值
	# Type: float
	# Unique: False, Required: False
	# Server: True, Client: True
	AnimationParamVariable = models.FloatField(default=0, null=True, blank=True)

	# Description: 动画参数2名字
	# Type: string
	# Unique: False, Required: False
	# Server: True, Client: True
	AnimationParam2Name = models.CharField(max_length=255, null=True, blank=True)

	# Description: 动画参数2数值
	# Type: float
	# Unique: False, Required: False
	# Server: True, Client: True
	AnimationParam2Variable = models.FloatField(default=0, null=True, blank=True)

	def __str__(self):
		return 'AnimationStatic: ' + str(self.id)

