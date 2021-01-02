/*
 Navicat Premium Data Transfer

 Source Server         : ayjin
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : qq

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 02/01/2021 17:51:01
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for logs
-- ----------------------------
DROP TABLE IF EXISTS `logs`;
CREATE TABLE `logs`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `reciver` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `message` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'nothing',
  `sendtime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 152 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of logs
-- ----------------------------
INSERT INTO `logs` VALUES (1, 'ayjin', 'ROBOT', 'nothing', '2020-12-23 01:23:06');
INSERT INTO `logs` VALUES (2, 'sender', 'reciver', 'test', '2020-12-23 01:37:21');
INSERT INTO `logs` VALUES (3, 'jluzh', 'Group chat', 'hello', '2020-12-23 01:40:06');
INSERT INTO `logs` VALUES (4, 'ayjin', 'test', 'hello', '2020-12-23 02:03:25');
INSERT INTO `logs` VALUES (5, 'jluzh', 'ayjin', '66666666666666666666666666666666666666666666666666666666666666666666', '2020-12-23 12:08:20');
INSERT INTO `logs` VALUES (6, 'jluzh', 'Group chat', '1', '2020-12-23 02:15:38');
INSERT INTO `logs` VALUES (7, 'jluzh', 'Group chat', '``#snow-mountain-wallpaper-2.jpg', '2020-12-23 10:56:24');
INSERT INTO `logs` VALUES (8, 'jluzh', 'Group chat', '大家好', '2020-12-23 11:04:48');
INSERT INTO `logs` VALUES (9, 'jluzh', 'Group chat', '我是？', '2020-12-23 11:04:51');
INSERT INTO `logs` VALUES (10, 'jluzh', 'Group chat', '我是测试数据哦', '2020-12-23 11:04:56');
INSERT INTO `logs` VALUES (11, 'jluzh', 'Group chat', 'ay1jin', '2020-12-23 11:05:18');
INSERT INTO `logs` VALUES (12, 'jluzh', 'Group chat', 'switch code', '2020-12-23 11:05:22');
INSERT INTO `logs` VALUES (13, 'jluzh', 'Group chat', 'less', '2020-12-23 11:05:24');
INSERT INTO `logs` VALUES (14, 'jluzh', 'Group chat', 'less than important', '2020-12-23 11:05:28');
INSERT INTO `logs` VALUES (15, 'jluzh', 'Robot', '在吗？', '2020-12-23 11:08:52');
INSERT INTO `logs` VALUES (16, 'jluzh', 'Group chat', 'aa**', '2020-12-23 11:33:59');
INSERT INTO `logs` VALUES (17, 'jluzh', 'Group chat', '2', '2020-12-23 13:56:26');
INSERT INTO `logs` VALUES (18, 'test1', 'jluzh', '1', '2020-12-23 13:56:56');
INSERT INTO `logs` VALUES (19, 'test1', 'jluzh', '1', '2020-12-23 13:56:56');
INSERT INTO `logs` VALUES (20, 'jluzh', 'test1', '1', '2020-12-23 13:57:06');
INSERT INTO `logs` VALUES (21, 'jluzh', 'test1', '1', '2020-12-23 13:57:06');
INSERT INTO `logs` VALUES (22, 'jluzh', 'test1', '2', '2020-12-23 13:57:56');
INSERT INTO `logs` VALUES (23, 'jluzh', 'test1', '2', '2020-12-23 13:57:56');
INSERT INTO `logs` VALUES (24, 'jluzh', 'test1', '1', '2020-12-23 13:58:03');
INSERT INTO `logs` VALUES (25, 'jluzh', 'test1', '1', '2020-12-23 13:58:03');
INSERT INTO `logs` VALUES (26, 'test1', 'jluzh', '在干嘛', '2020-12-23 14:04:08');
INSERT INTO `logs` VALUES (27, 'test1', 'jluzh', '在干嘛', '2020-12-23 14:04:08');
INSERT INTO `logs` VALUES (28, 'jluzh', 'test1', '你呢？', '2020-12-23 14:04:20');
INSERT INTO `logs` VALUES (29, 'jluzh', 'test1', '你呢？', '2020-12-23 14:04:20');
INSERT INTO `logs` VALUES (30, 'jluzh', 'test1', '在吃饭，我是jluzh', '2020-12-23 14:04:42');
INSERT INTO `logs` VALUES (31, 'jluzh', 'test1', '在吃饭，我是jluzh', '2020-12-23 14:04:42');
INSERT INTO `logs` VALUES (32, 'test1', 'jluzh', '在吃饭，我是test1', '2020-12-23 14:04:56');
INSERT INTO `logs` VALUES (33, 'test1', 'jluzh', '在吃饭，我是test1', '2020-12-23 14:04:56');
INSERT INTO `logs` VALUES (34, 'test1', 'jluzh', 'Im test', '2020-12-23 14:22:29');
INSERT INTO `logs` VALUES (35, 'test1', 'jluzh', 'Im test', '2020-12-23 14:22:29');
INSERT INTO `logs` VALUES (36, 'jluzh', 'Group chat', '``#1.png', '2020-12-23 15:15:50');
INSERT INTO `logs` VALUES (37, 'jluzh', 'Group chat', '``#1.png', '2020-12-23 15:24:34');
INSERT INTO `logs` VALUES (38, 'jluzh', 'Group chat', '``#1.png.png', '2020-12-23 15:29:35');
INSERT INTO `logs` VALUES (39, 'jluzh', 'Group chat', '``#addfriend.png', '2020-12-23 15:30:16');
INSERT INTO `logs` VALUES (40, 'jluzh', 'Group chat', '``#1.png', '2020-12-23 15:36:49');
INSERT INTO `logs` VALUES (41, 'jluzh', 'jluzh', '``#snow-mountain-wallpaper-2.jpg', '2020-12-23 15:37:12');
INSERT INTO `logs` VALUES (42, 'jluzh', 'Group chat', '``#addfriend.png', '2020-12-23 15:37:24');
INSERT INTO `logs` VALUES (43, 'jluzh', 'Group chat', 'aa**', '2020-12-23 15:37:32');
INSERT INTO `logs` VALUES (44, 'jluzh', 'Group chat', '``#concerned.png', '2020-12-23 15:38:01');
INSERT INTO `logs` VALUES (45, 'jluzh', 'Group chat', '``#facepalm.png', '2020-12-23 15:38:08');
INSERT INTO `logs` VALUES (46, 'jluzh', 'Group chat', '``#concerned.png', '2020-12-23 15:40:52');
INSERT INTO `logs` VALUES (47, 'jluzh', 'Group chat', '``#1.png', '2020-12-23 15:45:35');
INSERT INTO `logs` VALUES (48, 'jluzh', 'Group chat', '``#jluzh.jpg', '2020-12-23 15:45:47');
INSERT INTO `logs` VALUES (49, 'jluzh', 'Group chat', '``#addfriend.png', '2020-12-23 15:46:01');
INSERT INTO `logs` VALUES (50, 'jluzh', 'Group chat', '1', '2020-12-23 15:51:48');
INSERT INTO `logs` VALUES (51, 'jluzh', 'Robot', '1', '2020-12-23 15:52:11');
INSERT INTO `logs` VALUES (52, 'jluzh', 'Robot', '2', '2020-12-23 15:52:20');
INSERT INTO `logs` VALUES (53, 'jluzh', 'Robot', '你好', '2020-12-23 15:52:22');
INSERT INTO `logs` VALUES (54, 'jluzh', 'Robot', '你好', '2020-12-23 16:43:51');
INSERT INTO `logs` VALUES (55, 'jluzh', 'Robot', '你好', '2020-12-23 16:45:46');
INSERT INTO `logs` VALUES (56, 'jluzh', 'Robot', '你好', '2020-12-23 16:46:59');
INSERT INTO `logs` VALUES (57, 'jluzh', 'Robot', '你是谁呀？', '2020-12-23 16:47:09');
INSERT INTO `logs` VALUES (58, 'jluzh', 'Robot', '你是谁？', '2020-12-23 16:47:50');
INSERT INTO `logs` VALUES (59, 'jluzh', 'Robot', '讲个笑话呗', '2020-12-23 16:48:01');
INSERT INTO `logs` VALUES (60, 'jluzh', 'Robot', '来个图片', '2020-12-23 16:48:38');
INSERT INTO `logs` VALUES (61, 'jluzh', 'Robot', '', '2020-12-23 16:48:44');
INSERT INTO `logs` VALUES (62, 'jluzh', 'Robot', 'INVITE192.168.248.1', '2020-12-23 16:49:37');
INSERT INTO `logs` VALUES (63, 'jluzh', 'Robot', 'aa**', '2020-12-23 16:50:15');
INSERT INTO `logs` VALUES (64, 'jluzh', 'Robot', '你好', '2020-12-23 17:16:50');
INSERT INTO `logs` VALUES (65, 'jluzh', 'Robot', '讲个笑话', '2020-12-23 17:16:57');
INSERT INTO `logs` VALUES (66, 'jluzh', 'Robot', 'cc**', '2020-12-23 17:17:45');
INSERT INTO `logs` VALUES (67, 'jluzh', 'Robot', '在吗？', '2020-12-24 14:51:57');
INSERT INTO `logs` VALUES (68, 'jluzh', 'Robot', '你在干什么', '2020-12-24 14:52:04');
INSERT INTO `logs` VALUES (69, 'jluzh', 'Robot', '吃饭了吗', '2020-12-24 14:52:06');
INSERT INTO `logs` VALUES (70, 'jluzh', 'Robot', '吃的什么', '2020-12-24 14:52:08');
INSERT INTO `logs` VALUES (71, 'jluzh', 'Robot', '吃了几碗饭', '2020-12-24 14:52:17');
INSERT INTO `logs` VALUES (72, 'jluzh', 'Robot', '吃的什么菜', '2020-12-24 14:52:23');
INSERT INTO `logs` VALUES (73, 'jluzh', 'Group chat', '你好', '2020-12-24 15:01:56');
INSERT INTO `logs` VALUES (74, 'jluzh', 'Robot', '你好', '2020-12-24 15:02:06');
INSERT INTO `logs` VALUES (75, 'jluzh', 'Group chat', 'aa**', '2020-12-24 16:25:37');
INSERT INTO `logs` VALUES (76, 'jluzh', 'Robot', '我好无聊', '2020-12-24 19:40:27');
INSERT INTO `logs` VALUES (77, 'jluzh', 'Group chat', '', '2020-12-24 20:23:48');
INSERT INTO `logs` VALUES (78, 'jluzh', 'test1', '1', '2020-12-24 20:56:33');
INSERT INTO `logs` VALUES (79, 'jluzh', 'test1', '在吗？', '2020-12-24 20:56:38');
INSERT INTO `logs` VALUES (80, 'jluzh', 'Robot', '在吗?', '2020-12-24 20:57:44');
INSERT INTO `logs` VALUES (81, 'jluzh', 'Group chat', 'INVITE192.168.248.1', '2020-12-24 22:26:34');
INSERT INTO `logs` VALUES (82, 'jluzh', 'Group chat', 'INVITE192.168.248.1', '2020-12-24 22:26:34');
INSERT INTO `logs` VALUES (83, 'jluzh', 'test1', 'INVITE192.168.248.1', '2020-12-24 22:26:43');
INSERT INTO `logs` VALUES (84, 'jluzh', 'test1', 'INVITE192.168.248.1', '2020-12-24 22:26:43');
INSERT INTO `logs` VALUES (85, 'jluzh', 'Group chat', 'bb**', '2020-12-24 22:59:20');
INSERT INTO `logs` VALUES (86, 'jluzh', 'Robot', '你好啊', '2020-12-24 22:59:35');
INSERT INTO `logs` VALUES (87, 'jluzh', 'Robot', '在干嘛', '2020-12-24 22:59:40');
INSERT INTO `logs` VALUES (88, 'jluzh', 'Robot', '讲个笑话？', '2020-12-24 22:59:43');
INSERT INTO `logs` VALUES (89, 'jluzh', 'Robot', '你三围多少', '2020-12-24 22:59:55');
INSERT INTO `logs` VALUES (90, 'jluzh', 'Robot', '谢伟林帅吗', '2020-12-24 23:00:06');
INSERT INTO `logs` VALUES (91, 'jluzh', 'Robot', '你会唱歌吗？', '2020-12-24 23:00:13');
INSERT INTO `logs` VALUES (92, 'jluzh', 'Robot', '你觉得你聪明嘛?', '2020-12-24 23:00:57');
INSERT INTO `logs` VALUES (93, 'jluzh', 'Robot', 'wo cao nima de', '2020-12-24 23:01:03');
INSERT INTO `logs` VALUES (94, 'jluzh', 'Robot', '我操你妈的‘', '2020-12-24 23:01:15');
INSERT INTO `logs` VALUES (95, 'jluzh', 'Robot', '尼玛死了', '2020-12-24 23:01:17');
INSERT INTO `logs` VALUES (96, 'jluzh', 'Robot', '我原谅尼玛B', '2020-12-24 23:01:23');
INSERT INTO `logs` VALUES (97, 'jluzh', 'Robot', '操年迈的', '2020-12-24 23:01:25');
INSERT INTO `logs` VALUES (98, 'jluzh', 'Robot', '我操哦', '2020-12-24 23:01:27');
INSERT INTO `logs` VALUES (99, 'jluzh', 'Robot', '我操', '2020-12-24 23:01:29');
INSERT INTO `logs` VALUES (100, 'jluzh', 'Robot', '掉尼玛个害', '2020-12-24 23:01:34');
INSERT INTO `logs` VALUES (101, 'jluzh', 'Robot', '小心我顺着网线爬过去吧你杀了', '2020-12-24 23:01:45');
INSERT INTO `logs` VALUES (102, 'jluzh', 'Robot', '好久不见哦', '2020-12-29 02:46:13');
INSERT INTO `logs` VALUES (103, 'jluzh', 'jluzh_2', 'INVITE192.168.248.1', '2020-12-29 15:01:05');
INSERT INTO `logs` VALUES (104, 'jluzh', 'jluzh_2', 'INVITE192.168.248.1', '2020-12-29 15:01:05');
INSERT INTO `logs` VALUES (105, 'jluzh', 'jluzh_2', 'INVITE192.168.248.1', '2020-12-29 15:01:15');
INSERT INTO `logs` VALUES (106, 'jluzh', 'jluzh_2', 'INVITE192.168.248.1', '2020-12-29 15:01:15');
INSERT INTO `logs` VALUES (107, 'jluzh', 'Group chat', 'INVITE192.168.248.1', '2020-12-29 15:01:28');
INSERT INTO `logs` VALUES (108, 'jluzh', 'Group chat', 'INVITE192.168.248.1', '2020-12-29 15:01:28');
INSERT INTO `logs` VALUES (109, 'jluzh', 'test1', 'INVITE192.168.248.1', '2020-12-29 15:02:10');
INSERT INTO `logs` VALUES (110, 'jluzh', 'test1', 'INVITE192.168.248.1', '2020-12-29 15:02:10');
INSERT INTO `logs` VALUES (111, 'jluzh', 'Robot', '你好，在干嘛?', '2020-12-29 15:06:23');
INSERT INTO `logs` VALUES (112, 'jluzh', 'Robot', '吃饭没？', '2020-12-29 15:06:34');
INSERT INTO `logs` VALUES (113, 'jluzh', 'Robot', '吃的什么', '2020-12-29 15:06:36');
INSERT INTO `logs` VALUES (114, 'jluzh', 'Robot', '讲个笑话', '2020-12-29 15:06:43');
INSERT INTO `logs` VALUES (115, 'jluzh', 'Robot', '今天的天气怎么样', '2020-12-29 15:07:00');
INSERT INTO `logs` VALUES (116, 'jluzh', 'Robot', '广东', '2020-12-29 15:07:04');
INSERT INTO `logs` VALUES (117, 'jluzh', 'Robot', '广东天气怎么样', '2020-12-29 15:07:13');
INSERT INTO `logs` VALUES (118, 'jluzh', 'Robot', '吃饭了吗', '2020-12-29 15:07:21');
INSERT INTO `logs` VALUES (119, 'jluzh', 'test1', '在吗？', '2020-12-29 15:22:56');
INSERT INTO `logs` VALUES (120, 'jluzh', 'test1', '在吗？', '2020-12-29 15:22:56');
INSERT INTO `logs` VALUES (121, 'test1', 'Group chat', 'bb**', '2020-12-29 15:22:59');
INSERT INTO `logs` VALUES (122, 'test1', 'Group chat', 'bb**', '2020-12-29 15:22:59');
INSERT INTO `logs` VALUES (123, 'jluzh', 'Robot', '吃饭没', '2020-12-29 15:23:09');
INSERT INTO `logs` VALUES (124, 'jluzh', 'Robot', '吃饭没', '2020-12-29 15:23:09');
INSERT INTO `logs` VALUES (125, 'jluzh', 'Robot', '我好无聊。', '2020-12-29 15:23:14');
INSERT INTO `logs` VALUES (126, 'jluzh', 'Robot', '我好无聊。', '2020-12-29 15:23:14');
INSERT INTO `logs` VALUES (127, 'jluzh', 'Robot', '``#Risk Management.png', '2020-12-29 15:23:39');
INSERT INTO `logs` VALUES (128, 'jluzh', 'Robot', '``#Risk Management.png', '2020-12-29 15:23:39');
INSERT INTO `logs` VALUES (129, 'jluzh', 'Robot', '``#addfriend.png', '2020-12-29 15:23:56');
INSERT INTO `logs` VALUES (130, 'jluzh', 'Robot', '``#addfriend.png', '2020-12-29 15:23:56');
INSERT INTO `logs` VALUES (131, 'jluzh', 'Robot', 'INVITE192.168.248.1', '2020-12-29 15:24:34');
INSERT INTO `logs` VALUES (132, 'jluzh', 'Robot', 'INVITE192.168.248.1', '2020-12-29 15:24:34');
INSERT INTO `logs` VALUES (133, 'jluzh', 'test1', 'INVITE192.168.248.1', '2020-12-29 15:24:45');
INSERT INTO `logs` VALUES (134, 'jluzh', 'test1', 'INVITE192.168.248.1', '2020-12-29 15:24:45');
INSERT INTO `logs` VALUES (135, 'jluzh', 'Robot', '差不多就这些了。', '2020-12-29 15:27:57');
INSERT INTO `logs` VALUES (136, 'jluzh', 'test1', '在？', '2021-01-02 17:06:07');
INSERT INTO `logs` VALUES (137, 'jluzh', 'test1', '在？', '2021-01-02 17:06:07');
INSERT INTO `logs` VALUES (138, 'test1', 'jluzh', '在的。', '2021-01-02 17:06:15');
INSERT INTO `logs` VALUES (139, 'test1', 'jluzh', '在的。', '2021-01-02 17:06:15');
INSERT INTO `logs` VALUES (140, 'jluzh', 'test1', 'aa**', '2021-01-02 17:06:24');
INSERT INTO `logs` VALUES (141, 'jluzh', 'test1', 'aa**', '2021-01-02 17:06:24');
INSERT INTO `logs` VALUES (142, 'jluzh', 'test1', '``#1.png', '2021-01-02 17:06:37');
INSERT INTO `logs` VALUES (143, 'jluzh', 'test1', '``#1.png', '2021-01-02 17:06:37');
INSERT INTO `logs` VALUES (144, 'jluzh', 'test1', '``#addfriend.png', '2021-01-02 17:06:50');
INSERT INTO `logs` VALUES (145, 'jluzh', 'test1', '``#addfriend.png', '2021-01-02 17:06:50');
INSERT INTO `logs` VALUES (146, 'jluzh', 'Robot', '在干嘛？', '2021-01-02 17:07:01');
INSERT INTO `logs` VALUES (147, 'jluzh', 'Robot', '在干嘛？', '2021-01-02 17:07:01');
INSERT INTO `logs` VALUES (148, 'jluzh', 'Robot', 'INVITE192.168.248.1', '2021-01-02 17:07:23');
INSERT INTO `logs` VALUES (149, 'jluzh', 'Robot', 'INVITE192.168.248.1', '2021-01-02 17:07:23');
INSERT INTO `logs` VALUES (150, 'jluzh', 'test1', 'INVITE192.168.248.1', '2021-01-02 17:07:30');
INSERT INTO `logs` VALUES (151, 'jluzh', 'test1', 'INVITE192.168.248.1', '2021-01-02 17:07:30');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `passwd` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'ayjin', 'ayjin');
INSERT INTO `user` VALUES (2, 'jluzh', 'jluzh');
INSERT INTO `user` VALUES (3, 'test1', 'test1');
INSERT INTO `user` VALUES (4, 'asd', 'asd');

SET FOREIGN_KEY_CHECKS = 1;
