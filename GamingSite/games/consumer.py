from channels.generic.websocket import AsyncWebsocketConsumer
import json
import time
from .views import othello_models


class OthelloLobby(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "_".join(self.scope["path"].split("/"))
        print(self.room_group_name)

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))


class OthelloDuel(AsyncWebsocketConsumer):
    async def connect(self):
        q = self.scope["path"].split("/")
        self.room_group_name = "_".join(q[1:5])
        self.room_id = int(q[-3])
        self.model = othello_models[self.room_id]
        print(self.room_group_name, self.room_id)

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        category = text_data_json["category"]

        if category == "move":
            move = text_data_json["value"]
            if move == -1:
                self.model.back()
            elif move == -2:
                self.model.initialize()
            else:
                self.model.update(move)

            board = []
            for row in self.model.board.b:
                for element in row:
                    board.append(element)
            status = [self.model.board.wn, self.model.board.bn, self.model.board.turn, self.model.end]

            await self.channel_layer.group_send(
                self.room_group_name, {"type": "after_move", "board": board, "status": status}
            )
        else:
            message = text_data_json["value"]
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "message": message}
            )

    async def after_move(self, event):
        await self.send(text_data=json.dumps({"category": "move", "board": event["board"], "status": event["status"]}))

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"category": "chat", "message": event["message"]}))


class OthelloAI(AsyncWebsocketConsumer):
    async def connect(self):
        q = self.scope["path"].split("/")
        self.room_group_name = "_".join(q[1:6])
        self.room_id = int(q[-3])
        self.model = othello_models[self.room_id]
        print(self.room_group_name, self.room_id)

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        category = text_data_json["category"]

        if category == "move":
            move = text_data_json["value"]
            print(move, self.room_id)
            if move == -1:
                self.model.back()
            elif move == -2:
                self.model.initialize()
            elif move == -3:
                time.sleep(1)
                if self.room_id < 4:
                    print("greedy")
                    self.model.play_ai_greedy()
                elif self.room_id < 8:
                    print("minimax")
                    self.model.play_ai_minimax()
                else:
                    print("improved")
                    self.model.play_ai_improved()
            else:
                self.model.update(move)

            board = []
            for row in self.model.board.b:
                for element in row:
                    board.append(element)
            status = [self.model.board.wn, self.model.board.bn, self.model.board.turn, self.model.end, self.model.ai]

            await self.channel_layer.group_send(
                self.room_group_name, {"type": "after_move", "board": board, "status": status}
            )
        else:
            message = text_data_json["value"]
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "message": message}
            )

    async def after_move(self, event):
        await self.send(text_data=json.dumps({"category": "move", "board": event["board"], "status": event["status"]}))

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"category": "chat", "message": event["message"]}))
