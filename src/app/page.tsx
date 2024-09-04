"use client";

import DragDrop from "@/components/InputFields/DragDrop";
import { Layout, Menu, theme } from "antd";
import React from "react";
import { IoChatboxEllipsesOutline, IoSettingsOutline } from "react-icons/io5";
import { MdOutlineAnalytics } from "react-icons/md";
import { RiMessage2Line } from "react-icons/ri";
import { RxDashboard } from "react-icons/rx";

const { Header, Content, Footer, Sider } = Layout;

const items = [
  { key: "1", icon: <RxDashboard />, label: "Dashboard" },
  { key: "2", icon: <IoChatboxEllipsesOutline />, label: "Chat" },
  { key: "3", icon: <MdOutlineAnalytics />, label: "Analytics" },
  { key: "4", icon: <RiMessage2Line />, label: "Message" },
  { key: "5", icon: <IoSettingsOutline />, label: "Settings" },
];

const App: React.FC = () => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  return (
    <Layout className="h-full">
      <Sider
        breakpoint="lg"
        collapsedWidth="0"
        onBreakpoint={(broken) => {
          console.log(broken);
        }}
        onCollapse={(collapsed, type) => {
          console.log(collapsed, type);
        }}
      >
        <div className="demo-logo-vertical" />
        <Menu
          theme="dark"
          mode="inline"
          defaultSelectedKeys={["1"]}
          items={items}
        />
      </Sider>
      <Layout>
        <Header
          style={{ padding: 0, background: "#13171C" }}
          className="flex items-center"
        >
          <p className="text-3xl ml-2 font-semibold font-mono">
            <span className="text-[#2DE70F]">CROP</span>
            <span className="text-white">DEX</span>
          </p>
        </Header>
        <Content style={{ margin: "24px 16px 0" }}>
          <div
            className="h-full"
            style={{
              padding: 24,
              background: colorBgContainer,
              borderRadius: borderRadiusLG,
            }}
          >
            <div className="flex flex-col gap-5">
              <p className=" font-mono font-semibold text-3xl">
                Insert your image :
              </p>
              <div>
                <DragDrop />
              </div>
            </div>
          </div>
        </Content>
        <Footer style={{ textAlign: "center" }}>
          Ant Design ©{new Date().getFullYear()} Created by Ant UED
        </Footer>
      </Layout>
    </Layout>
  );
};

export default App;
